#!/usr/bin/env python3
####### PACKAGES
import sys, os

__index__ = "index.md"
__template__ = "index_template.md"
__sc_file__ = "pages/science.md"
__sc_fold__ = "pages/science"
__blog_file__ = "pages/blog.md"
__blog_fold__ = "pages/blog"
__soc_file__ = "pages/society.md"
__soc_fold__ = "pages/society"

__N_elems__ = 3

__WEIGHT__ = "__WEIGHT__"
__TITLE__ = "__TITLE__"
__INSERT_HERE__  = "__INSERT_HERE__"
def make_element(file):
    weight = 0
    title = None
    with open(file, "r") as content:
        lines = content.readlines()
        for line in lines:
            w = line.find(__WEIGHT__) 
            if w>0:
                w = w+10
                words = line[w:]
                words = words.split(")")[0]
                weight = float(words)
            t = line.find(__TITLE__) 
            if t>0:
                t = t+9
                words = line[t:]
                words = words.split(")")[:-1]
                title = "".join(words)
    print((weight, title, file))
    return (weight, title, file)

def make_ranking(folder):
    liste = []
    for file in os.listdir(folder):
        if file.endswith(".md"):
            path = "%s/%s" %(folder, file)
            liste.append(make_element(path))
    kept = [element for element in liste if element[1] is not None]
    kept.sort(key=lambda el: el[0])
    return kept
        
def make_page(fname, elements, title):
    with open(fname, "w") as file:
        file.write("# %s \n"%title)
        for el in elements:
            link = "%s" %el[2]
            if link.startswith("pages/"):
                link = link[6:]
            file.write("- [%s](%s) \n" %(el[1],link))

if __name__ == "__main__":
    to_sort = {"Science" : [__sc_file__, __sc_fold__],
                "Blog" : [__blog_file__, __blog_fold__],
                "Society" : [__soc_file__, __soc_fold__]
                }

    topics = []

    lines = []

    def stash_to_index(elements, title):
        lines.append("## %s" %title)
        for el in elements[0:__N_elems__]:
            lines.append("- [%s](%s) \n" % (el[1], el[2]))
        #lines.append("\n")

    for key, item in to_sort.items():
        ranked = make_ranking(item[1])
        topics.append(ranked)
        make_page(item[0], ranked, key)
        stash_to_index(ranked, key)

    with open(__index__,"w") as index:
        with open(__template__,"r") as template:
            tl = template.readlines()
            for l in tl:
                if l.find(__INSERT_HERE__)>0:
                    for ll in lines:
                        index.write(ll)
                        index.write(" \n")
                else:
                    index.write(l)
