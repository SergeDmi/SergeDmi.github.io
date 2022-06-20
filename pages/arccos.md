In a code I’m developping ([elastic model of discretized shells](https://github.com/SergeDmi/LimeSurf)), I needed to have the arccos of a scalar products of two (normalized) vectors, n1 and n2. So I used :

```C++
 std::acos(n1.dot(n2)/(n1.norm()*n2.norm()))
```

This of course will work beautifully. Because of the normalization ```/(n1.norm()*n2.norm()))```, the argument of ```std::acos``` will be always smaller than one, in absolute value...  

Except, you know, finite precision arithmetic ! Indeed, once has a finite precision for double, so even if one should get x=1, we could get x just just just a pinch slightly bigger than 1.  

And, since my vectors very often have the same orientation, my code will crash because I’m taking the ```std::acos(w)``` for $x>1$ (even though it’s actually $x=1$).  

So the next thing you know, I have to be a bit more careful :  
```C++
 double safer_acos(double x) {
 if (x < -1.0) x = -1.0 ;
 else if (x > 1.0) x = 1.0 ;
 return acos(x) ;
 }
```

However, I have to compute a lot of safer_acos in my code. Like, many. So it’s slow. Very slow. First thing I can do is to use an approximation of acos, because some work really well, like Nvidia’s :
```C++
 double faster_acos(double x) {
 // Handbook of Mathematical Functions
 // M. Abramowitz and I.A. Stegun, Ed.
 double negate = double(x < 0);
 x = abs(x);
 double ret = -0.0187293;
 ret = ret * x;
 ret = ret + 0.0742610;
 ret = ret * x;
 ret = ret - 0.2121144;
 ret = ret * x;
 ret = ret + 1.5707288;
 ret = ret * std::sqrt(1.0-x);
 ret = ret - 2.0 * negate * ret;
 return negate * 3.14159265358979 + ret;
 }
```

Much faster ! Also, note that your compiler (at least gcc, probably any good compiler) will simplify the algebra for you, so you can keep it in 10 lines for clarity…  

However, I still need to add ```if (x > 1.0) x = 1.0 ;``` to make the code safe. But this will also make it slower (arguably not much, but...), since if are slow because of branch predictions. You can try ```x=std::min(x,1.0);```, but it’s not really faster.  

In the end, we can still use the standard trick of using (x>1.0) as a variable, which requires no branching. And we can write : ```x -= double(x>1.0)*(x-1.0);```. In the end, the fastest, non-crashing acos() I could find was : 
```C++
 double faster_safer_acos(double x) {
 double negate = double(x < 0);
 x = abs(x);
 x-= double(x>1.0)*(x-1.0);
 double ret = -0.0187293;
 ret = ret * x;
 ret = ret + 0.0742610;
 ret = ret * x;
 ret = ret - 0.2121144;
 ret = ret * x;
 ret = ret + 1.5707288;
 ret = ret * std::sqrt(1.0-x);
 ret = ret - 2.0 * negate * ret;
 return negate * 3.14159265358979 + ret;
 }
```

That was very simple but fun and informative : I was reminded to be careful of finite precision arithmetic, I realized that acos was slow (inverse function…), and remembered that although branching is slow, it can often be avoided !

