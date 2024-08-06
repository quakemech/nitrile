# Overview 

The nitrile python module provides the ability to create Latex source documents
and compile them into PDF files. 

The general flow to create a Latex document is to perform the following actions:

1. Instantiate a nitrile.Document object
2. Add nitrile.Package objects using nitrile.Document.add()
3. Add nitrile.Command objects using nitrile.Document.add()
4. Add various forms of nitrile.Body objects using nitrile.Document.add()
5. Run the nitrile.Document.tex() or pdf() functions to assemble the 
   content into a Latex Document.

# Setup 

After cloning the repository, cd into the repo and create a Python virtual 
environment using:

```bash
virtualenv venv 
```

Then install library dependecies using the requirements file: 

```bash
pip3 install -r requirements.txt 
```

# Build documentation 

Documentation is built using sphinx 

# Usage Examples
            
The following are examples on how to use each of the nitrile classes in 
Documents

## Example: Hello World

Here is a basic example of on how to use a Document

```python
d = nitrile.Document(classname='report', options=['9pt', 'twoside'])
d.add("Hello, World!")
d.tex()
```

which produces the following Latex output

```latex
\\documentclass[9pt,twoside]{report}
\\begin{document}
Hello, World!
\\end{document}
```

## Example: Packages

Here is how to add packages to a Document

```python
d = nitrile.Document(classname='report', options=['9pt', 'twoside'])
d.add(Package('DejaVuSansMono'))
d.add(Package('inputenc', options=['utf8x']))
d.add("Hello, World!")
```

which produces the following Latex output

```latex
\\documentclass[9pt,twoside]{report}
\\usepackage{DejaVuSansMono}
\\usepackage[utf8x]{inputenc}
\\begin{document}
Hello, World!
\\end{document}
```

## Example: Commands

Here is how to add Commands to a Document

```python
d = nitrile.Document(classname='report', options=['9pt', 'twoside'])
d.add(Command('pagestyle', ['plain']))
d.add(Command('setlength', ['\\hoffset','-0.5 in']))
d.add("Hello, World!")
```

which produces the following Latex output

```latex
\\documentclass[9pt,twoside]{report}
\\pagestyle{plain}
\\setlength{\\hoffset}{-0.5 in}

\\begin{document}
Hello, World!
\\end{document}
```

## Example: Formatted / Unformatted Text 

Here is how to add math, **bold**, and *italic* statements to a Document

```python
d = nitrile.Document(classname='report', options=['9pt', 'twoside'])
d.add(Content('$\int_{a}^{b} x^2 dx$', 
              convert=False, 
              postnewlines=2))
              
d.add(Content('This content should be bold.', 
              bold=True, 
              postnewlines=2))
              
d.add(Content('This content should be italic.', 
              italic=True, 
              postnewlines=2))
```
    
which produces the following Latex output

```latex
\\documentclass[9pt,twoside]{report}
\\begin{document}
$\\int_{a}^{b} x^2 dx$

\\begin{bf}This content should be bold.\\end{bf}

\\begin{em}This content should be italic.\\end{em}

\\end{document}
```

## Example: Multicol Environment

Here is how to add an Environment (multicol) to a Document

```python
d = Document(   classname='report',
                options=['9pt', 'twoside'])

d.add(Package('multicol'))

d.add(Content('Example of multicol environment.', 
              postnewlines=1,
              noindent=True))
              
e = d.add(Environment('multicols', options='2'))

e.add(Content('This content should be in column 1 of the multicols '
              'environment.', 
              postnewlines=2,
              noindent=True))
      
e.add(Content('This content should be in column 2 of the multicols '
              'environment.', 
              postnewlines=0,
              noindent=True))
```
    
which produces the following Latex output

```latex
\\documentclass[9pt,twoside]{report}
\\usepackage{multicol}
\\begin{document}
\\noindent Example of multicol environment.

\\begin{multicols}{2}
\\noindent This content should be in column 1 of the multicols environment.

\\noindent This content should be in column 2 of the multicols environment.
\\end{multicols}

\\end{document}
```

## Example: Quote Environment

Here is how to add a Quote Environment to a Document

```python
d = Document(   classname='report',
                options=['9pt', 'twoside'])

d.add(Content('This is an example of a quote', 
              noindent=True))

e = d.add(Environment('quote'))

e.add(Content('Four score and seven years ago our fathers brought '
              'forth on this continent, a new nation . . .', 
              postnewlines=2))
              
e.add("Now we are engaged in a great civil war, testing whether that "
      "nation, or any nation. . .")
      
d.add(Content('Here is the next line after the quote.',
                  noindent=True))                                
```
    
which produces the following Latex output

```latex
\\documentclass[9pt,twoside]{report}
\\begin{document}
\\noindent This is an example of a quote
\\begin{quote}
Four score and seven years ago our fathers brought forth on this continent, a new nation . . .

Now we are engaged in a great civil war, testing whether that nation, or any nation. . .
\\end{quote}
\\noindent Here is the next line after the quote.
\\end{document}
```
    
## Example: Lists

Here is how to add a Quote Environment to a Document

```python
d = Document(   classname='report',
                options=['9pt', 'twoside'])    

d.add(Content('This is an example of an Itemized list',
              noindent=True))

i = d.add(Itemize(tight=False))
i.add('first')
i.add('second')
i.add('third')

d.add(Content('This is an example of a tight Enumerated list',
              noindent=True))
              
e = d.add(Enumerate(tight=True))
e.add('first')
e.add('second')
e.add('third')
```
    
which produces the following Latex output
    
```latex
\\documentclass[9pt,twoside]{report}
\\begin{document}
\\noindent This is an example of an Itemized list
\\begin{itemize}
\\item first
\\item second
\\item third
\\end{itemize}
\\noindent This is an example of a tight Enumerated list
\\begin{enumerate} \\setlength{\\itemsep}{0cm} \\setlength{\\parskip}{0cm}
\\item first
\\item second
\\item third
\\end{enumerate}

\\end{document}
```

## Example: Chapters

Here is how to add Chapters with Sections, SubSections, and SubSubsections 
to a Document

```python
d = Document(   classname='report',
                options=['9pt', 'twoside'])    

d.add('This content should be on the first page')

c = d.add(Chapter("ChapterName", 
                  clearpage=False,
                  cleardoublepage=False, 
                  label='1', 
                  numbered=True))

c.add('This text is part of the Chapter')

s = c.add(Section("SectionName", 
                  clearpage=False,
                  cleardoublepage=False, 
                  label='1.1', 
                  numbered=True))

s.add('This text is part of Section 1.1')

ss = s.add(SubSection('SubSectionName', 
                      clearpage=False,
                      cleardoublepage=False, 
                      label='1.1.1', 
                      numbered=True))

ss.add('This text is part of SubSection 1.1.1')
            
sss = ss.add(SubSubSection('SubSubSectionName', 
                           clearpage=False,
                           cleardoublepage=False, 
                           label='1.1.1.1', 
                           numbered=True))

sss.add('This text is part of SubSubSection 1.1.1.1')
```

which produces the following Latex output

```latex
\\documentclass[9pt,twoside]{report}
\\begin{document}
This content should be on the first page
\\chapter{ChapterName}\\label{1}
This text is part of the Chapter
\\section{SectionName}\\label{1.1}
This text is part of Section 1.1
\\subsection{SubSectionName}\\label{1.1.1}
This text is part of SubSection 1.1.1
\\subsubsection{SubSubSectionName}\\label{1.1.1.1}
This text is part of SubSubSection 1.1.1.1
\\end{document}
```

## Example: Sections

Here is how to add Sections, SubSections, and SubSubsections to a 
Document

```python
d = Document(   classname='article',
                options=['9pt', 'twoside'])    

s = d.add(Section("SectionName", 
                  clearpage=False,
                  cleardoublepage=False, 
                  label='1', 
                  numbered=True))

s.add('This text is part of Section 1')

ss = s.add(SubSection('SubSectionName', 
                      clearpage=False,
                      cleardoublepage=False, 
                      label='1.1', 
                      numbered=True))

ss.add('This text is part of SubSection 1.1')
            
sss = ss.add(SubSubSection('SubSubSectionName', 
                           clearpage=False,
                           cleardoublepage=False, 
                           label='1.1.1', 
                           numbered=True))

sss.add('This text is part of SubSubSection 1.1.1')
```
    
which produces the following Latex output

```latex
\\documentclass[9pt,twoside]{article}
\\begin{document}
\\section{SectionName}\\label{1}
This text is part of Section 1
\\subsection{SubSectionName}\\label{1.1}
This text is part of SubSection 1.1
\\subsubsection{SubSubSectionName}\\label{1.1.1}
This text is part of SubSubSection 1.1.1
\\end{document}
```

## Example: Tables

Here is how to use Tables

```python
d = Document(   classname='report',
                options=['9pt', 'twoside'])    

d.add(Package('tabularx'))

d.add(Content('Here is an example of a table with different three '
              'columns. The first column width is just wider than the tex. The'
              ' second and third column widths are variable.',
              noindent=True))

t = d.add(Table(columnparameters='| l | C | R | '))

r = t.add(Row())
r.add('aaa')
r.add('bbb')
r.add('ccc')

t.add(Tag('hline'))

r = t.add(Row())
r.add('aaaaa')
r.add('bbbbb')
r.add('ccccc')

r = t.add(Row())
r.add('aaaaaaa')
r.add('bbbbbbb')
r.add('ccccccc')

d.add(Content('The second table removes the space between '
              'the first and second column so that it appears that '
              'they are actually one column.', 
              prenewlines=2,
              noindent=True))

t = d.add(Table(columnparameters='| r @{} L | c | '))

r = t.add(Row())
r.add('ddd')
r.add('eee')
r.add('fff')

t.add(Tag('hline'))

r = t.add(Row())
r.add('ddddd')
r.add('eeeee')
r.add('fffff')

r = t.add(Row())
r.add('ddddddd')
r.add('eeeeeee')
r.add('fffffff')        
```

which produces the following Latex output

```latex
\\documentclass[9pt,twoside]{report}
\\usepackage{tabularx}
\\begin{document}
\\noindent Here is an example of a table with different three columns. 
The first column width is just wider than the tex. The second and 
third column widths are variable.

\\noindent \\begin{tabularx} {\\columnwidth}{| l | >{\\centering\\arraybackslash}X | >{\\raggedleft\\arraybackslash}X | }
aaa & bbb & ccc \\\\
\\hline
aaaaa & bbbbb & ccccc \\\\
aaaaaaa & bbbbbbb & ccccccc \\\\
\\end{tabularx} 

\\noindent The second table removes the space between the first and 
second column so that it appears that they are actually one column.
\\noindent \\begin{tabularx} {\\columnwidth}{| r @{} >{\\raggedright\\arraybackslash}X | c | }
ddd & eee & fff \\\\
\\hline
ddddd & eeeee & fffff \\\\
ddddddd & eeeeeee & fffffff \\\\
\\end{tabularx} 
\\end{document}
```

## Example: Figures

Here is how to use a Figure 

```python
d = Document(   classname='report',
                options=['9pt', 'twoside'])    

d.add(Package('graphicx'))

d.add(Content('This is an example of a figure', 
              postnewlines=1,
              noindent=True))

f = d.add(Figure(imagefilename='logo.png', 
                 star=False, 
                 width='0.25\\columnwidth', 
                 placement='htb', 
                 center=True, 
                 caption='This is the figure caption', 
                 label='fig:Example'))
```

which produces the following Latex output

```latex
\\documentclass[9pt,twoside]{report}
\\usepackage{graphicx}
\\begin{document}
\\noindent This is an example of a figure
\\begin{figure}[htb]
\\begin{center}
\\includegraphics[width=0.25\\columnwidth]{/Users/24832/Dropbox/Work/code/nitrile/nitrile/logo.png}\\\\\\end{center}
\\caption{This is the figure caption}
\\label{fig:Example}
\\end{figure}
\\end{document}
```

## Example: SubFigures

Here is how to use SubFigures

```python
d = Document(   classname='report',
                options=['9pt', 'twoside'])    

d.add(Package('graphicx'))
d.add(Package('subcaption'))

f = d.add(Figure(placement='t', 
                 center=True, 
                 caption='This is the whole figure caption', 
                 label='fig:Example'))
                 
f.add(SubFigure(    imagefilename='logo.png', 
                    subfigurewidth='0.49\\textwidth',
                    imagewidth='\\textwidth',
                    placement='t',
                    center=True,
                    caption='SubFigureA',
                    label='fig:Example'))
                    
f.add(SubFigure(    imagefilename='logo.png',
                    subfigurewidth='0.49\\textwidth',
                    imagewidth='\\textwidth',
                    placement='t',
                    center=True,
                    caption='SubFigureB',
                    label='fig:Example'))
```

which produces the following Latex output

```latex
\\documentclass[9pt,twoside]{report}
\\usepackage{graphicx}
\\usepackage{subcaption}
\\begin{document}
\\begin{figure}[t]
\\begin{center}
\\begin{subfigure}[t]{0.49\\textwidth}
\\centering
\\includegraphics[width=\\textwidth]{/Users/24832/Dropbox/Work/code/nitrile/nitrile/logo.png}\\\\
\\caption{SubFigureA}
\\label{fig:Example}
\\end{subfigure}
\\begin{subfigure}[t]{0.49\\textwidth}
\\centering
\\includegraphics[width=\\textwidth]{/Users/24832/Dropbox/Work/code/nitrile/nitrile/logo.png}\\\\
\\caption{SubFigureB}
\\label{fig:Example}
\\end{subfigure}
\\end{center}
\\caption{This is the whole figure caption}
\\label{fig:Example}
\\end{figure}
\\end{document}
```

## Example: Pictures

Here is how to use Picture

```python
d = Document(   classname='report',
                options=['9pt', 'twoside'])    

p = d.add(Picture(  width=80, 
                    height=70, 
                    unitlength='1mm', 
                    star=False,
                    placement='h',
                    caption='This is a drawing',
                    label='fig:Drawing'))

p.add('\\def\\gridspace{20}\\n')
p.add('\\def\\doublegridspace{40}\\n')
p.add('\\def\\griddiagonal{10}\\n')
p.add('\\def\\griddot{\\circle*{2}}\\n')
p.add('\\linethickness{1.5pt}\\n')

# dots
p.add(  '\\multiput(20, 10)(5, 5){3}'
        '{\\multiput(0, 0)(0, \\gridspace){3}'
        '{\\multiput(0, 0)(\\gridspace, 0){3}'
        '{\\griddot}}'
        '}\\n')

# straight lines
p.add(  '\\multiput(20, 10)(5, 5){3}'
        '{\\multiput(0, 0)(0, \\gridspace){3}'
        '{\\line(1, 0){\\doublegridspace}}'
        '\\multiput(0, 0)(\\gridspace, 0){3}'
        '{\\line(0, 1){\\doublegridspace}}'
        '}\\n')

# diagonal lines
p.add(  '\\multiput(20, 10)(0, \\gridspace){3}'
        '{\\multiput(0, 0)(\\gridspace, 0){3}'
        '{\\line(1, 1){\\griddiagonal}}'
        '}\\n')

p.add('\\linethickness{1pt}\\n')

# arrows
p.add('\\put(20, 10){\\vector(-1, -1){5}}\\n')
p.add('\\put(30, 60){\\vector(0, 1){10}}\\n')
p.add('\\put(70, 20){\\vector(1, 0){10}}\\n')

# labels
p.add('\\put(18, 12){\\makebox(0, 0){2}}\\n')
p.add('\\put(28, 62){\\makebox(0, 0){2}}\\n')
p.add('\\put(72, 22){\\makebox(0, 0){2}}\\n')
p.add('\\put(17, 4){\\makebox(0, 0){x}}\\n')
p.add('\\put(80, 18){\\makebox(0, 0){y}}\\n')
p.add('\\put(28, 70){\\makebox(0, 0){z}}\\n')
```

which produces the following Latex output

```latex
\\documentclass[9pt,twoside]{report}
\\begin{document}
\\setlength{\\unitlength}{1mm}
\\begin{figure}[h]
\\begin{center}
\\begin{picture}(80,70)
\\def\\gridspace{20}
\\def\\doublegridspace{40}
\\def\\griddiagonal{10}
\\def\\griddot{\\circle*{2}}
\\linethickness{1.5pt}
\\multiput(20, 10)(5, 5){3}{\\multiput(0, 0)(0, \\gridspace){3}{\\multiput(0, 0)(\\gridspace, 0){3}{\\griddot}}}
\\multiput(20, 10)(5, 5){3}{\\multiput(0, 0)(0, \\gridspace){3}{\\line(1, 0){\\doublegridspace}}\\multiput(0, 0)(\\gridspace, 0){3}{\\line(0, 1){\\doublegridspace}}}
\\multiput(20, 10)(0, \\gridspace){3}{\\multiput(0, 0)(\\gridspace, 0){3}{\\line(1, 1){\\griddiagonal}}}
\\linethickness{1pt}
\\put(20, 10){\\vector(-1, -1){5}}
\\put(30, 60){\\vector(0, 1){10}}
\\put(70, 20){\\vector(1, 0){10}}
\\put(18, 12){\\makebox(0, 0){2}}
\\put(28, 62){\\makebox(0, 0){2}}
\\put(72, 22){\\makebox(0, 0){2}}
\\put(17, 4){\\makebox(0, 0){x}}
\\put(80, 18){\\makebox(0, 0){y}}
\\put(28, 70){\\makebox(0, 0){z}}
\\end{picture}
\\caption{This is a drawing}
\\end{center}
\\label{fig:Drawing}
\\end{figure}
\\end{document}
```

## Example: Two Figures in multicol Environment 

Here is the code to add two figures to a multicol environment. Note that 
the `float` package needed to be added to allow figures to be added to 
the multicol environment. If the `float` package is omitted then latex 
will issue an error such as `Package multicol Warning: Floats and 
marginpars not allowed inside multicols environment!` and then not include 
the figures in the pdf output.

```python
d = Document(   classname='report',
                options=['9pt', 'twoside'])    

d.add(Package('multicol'))
d.add(Package('graphicx'))
d.add(Package('float'))

d.add(Content('This is an example of two figures in a '
              'multicolumn Environment.', 
              postnewlines=1, 
              noindent=True))
        
e = d.add(Environment('multicols', options='2'))

f = e.add(Figure(imagefilename='logo.png', 
                 star=False,
                 width='0.25\\columnwidth',
                 placement='H',
                 center=True,
                 caption='This is figure 1 caption',
                 label='fig:Example1'))
        
f = e.add(Figure(imagefilename='logo.png',
                 star=False,
                 width='0.25\\columnwidth',
                 placement='H',
                 center=True,
                 caption='This is figure 2 caption',
                 label='fig:Example2'))
```

which produces the following Latex output

```latex
\\documentclass[9pt,twoside]{report}
\\usepackage{multicol}
\\usepackage{graphicx}
\\usepackage{float}
\\begin{document}
\\noindent This is an example of two figures in a multicolumn Environment.
\\begin{multicols}{2}
\\begin{figure}[H]
\\begin{center}
\\includegraphics[width=0.25\\columnwidth]{/Users/24832/Dropbox/Work/code/nitrile/nitrile/logo.png}\\\\\\end{center}
\\caption{This is figure 1 caption}
\\label{fig:Example1}
\\end{figure}
\\begin{figure}[H]
\\begin{center}
\\includegraphics[width=0.25\\columnwidth]{/Users/24832/Dropbox/Work/code/nitrile/nitrile/logo.png}\\\\\\end{center}
\\caption{This is figure 2 caption}
\\label{fig:Example2}
\\end{figure}
\\end{multicols}
\\end{document}
```

## Example: maketitle

Here is how to add a title, author and date to the preamble

```python
d = Document(   classname='report',
                options=['9pt', 'twoside'])    

d.add(Command('title', ['Document Title']))
d.add(Command('author', ['Author Name']))
d.add(Command('date', ['2016-02-29']))        
d.add(Tag('maketitle'))
```
        
which produces the following Latex output

```latex
\\documentclass[9pt,twoside]{report}
\\title{Document Title}
\\author{Author Name}
\\date{2016-02-29}
\\begin{document}
\\maketitle
\\end{document}
```
