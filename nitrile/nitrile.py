#!/usr/bin/python
# SPDX-License-Identifier: Apache-2.0 
# ******************************************************************************
#
# @file			nitrile.py
#
# @brief        Nitrile library code file
#
# @copyright    Copyright (C) 2024 Barrett Edwards. All rights reserved.
#
# @date         Aug 2024
# @author       Barrett Edwards <thequakemech@gmail.com>
# 
# ******************************************************************************

""" 
    The nitrile module provides the ability to create Latex source documents
    and compile them into PDF files. 
    
    To create a Latex document, perform the following actions: 

    1. Instantiate a nitrile.Document object
    2. Add nitrile.Package objects using nitrile.Document.add()
    3. Add nitrile.Command objects using nitrile.Document.add()
    4. Add various forms of nitrile.Body objects using nitrile.Document.add()
    5. Run the nitrile.Document.tex() or pdf() functions to assemble the 
       content into a Latex Document.
    
    ---------
     Examples
    ---------
            
    The following are examples on how to use each of the nitrile classes in 
    Documents


    Example: Hello World
    ^^^^^^^^^^^^^^^^^^^^

    Here is a basic example of on how to use a Document::

        d = nitrile.Document(classname='report', options=['9pt', 'twoside'])
        d.add("Hello, World!")
        d.tex()

    which produces the following Latex output::

        \\documentclass[9pt,twoside]{report}
        \\begin{document}
        Hello, World!
        \\end{document}


    Example: Packages
    ^^^^^^^^^^^^^^^^^

    Here is how to add packages to a Document::

        d = nitrile.Document(classname='report', options=['9pt', 'twoside'])
        d.add(Package('DejaVuSansMono'))
        d.add(Package('inputenc', options=['utf8x']))
        d.add("Hello, World!")

    which produces the following Latex output::

        \\documentclass[9pt,twoside]{report}
        \\usepackage{DejaVuSansMono}
        \\usepackage[utf8x]{inputenc}
        \\begin{document}
        Hello, World!
        \\end{document}

 
    Example: Commands
    ^^^^^^^^^^^^^^^^^

    Here is how to add Commands to a Document::

        d = nitrile.Document(classname='report', options=['9pt', 'twoside'])
        d.add(Command('pagestyle', ['plain']))
        d.add(Command('setlength', ['\\hoffset','-0.5 in']))
        d.add("Hello, World!")

    which produces the following Latex output::

        \\documentclass[9pt,twoside]{report}
        \\pagestyle{plain}
        \\setlength{\\hoffset}{-0.5 in}

        \\begin{document}
        Hello, World!
        \\end{document}


    Example: Formatted / Unformatted Text 
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Here is how to add math, **bold**, and *italic* statements to a Document::

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
        
    which produces the following Latex output::

        \\documentclass[9pt,twoside]{report}
        \\begin{document}
        $\\int_{a}^{b} x^2 dx$

        \\begin{bf}This content should be bold.\\end{bf}

        \\begin{em}This content should be italic.\\end{em}


        \\end{document}


    Example: Multicol Environment
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Here is how to add an Environment (multicol) to a Document::

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
        
    which produces the following Latex output::

        \\documentclass[9pt,twoside]{report}
        \\usepackage{multicol}
        \\begin{document}
        \\noindent Example of multicol environment.

        \\begin{multicols}{2}
        \\noindent This content should be in column 1 of the multicols environment.

        \\noindent This content should be in column 2 of the multicols environment.
        \\end{multicols}

        \\end{document}


    Example: Quote Environment
    ^^^^^^^^^^^^^^^^^^^^^^^^^^

    Here is how to add a Quote Environment to a Document::
    
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
        
    which produces the following Latex output::
    
        \\documentclass[9pt,twoside]{report}
        \\begin{document}
        \\noindent This is an example of a quote
        \\begin{quote}
        Four score and seven years ago our fathers brought forth on this continent, a new nation . . .

        Now we are engaged in a great civil war, testing whether that nation, or any nation. . .
        \\end{quote}
        \\noindent Here is the next line after the quote.
        \\end{document}
        
        
    Example: Lists
    ^^^^^^^^^^^^^^

    Here is how to add a Quote Environment to a Document::
    
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
        
    which produces the following Latex output::
        
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


    Example: Chapters
    ^^^^^^^^^^^^^^^^^

    Here is how to add Chapters with Sections, SubSections, and SubSubsections 
    to a Document::
    
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
    
    which produces the following Latex output::    
    
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
    

    Example: Sections
    ^^^^^^^^^^^^^^^^^

    Here is how to add Sections, SubSections, and SubSubsections to a 
    Document::
    
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
        
    which produces the following Latex output::

        \\documentclass[9pt,twoside]{article}
        \\begin{document}
        \\section{SectionName}\\label{1}
        This text is part of Section 1
        \\subsection{SubSectionName}\\label{1.1}
        This text is part of SubSection 1.1
        \\subsubsection{SubSubSectionName}\\label{1.1.1}
        This text is part of SubSubSection 1.1.1
        \\end{document}


    Example: Tables
    ^^^^^^^^^^^^^^^

    Here is how to use Tables::
    
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

    which produces the following Latex output::

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



    Example: Figures
    ^^^^^^^^^^^^^^^^

    Here is how to use a Figure ::
 
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
 
    which produces the following Latex output:: 

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


    Example: SubFigures
    ^^^^^^^^^^^^^^^^^^^
    
    Here is how to use SubFigures::

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

    which produces the following Latex output::
    
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


    Example: Pictures
    ^^^^^^^^^^^^^^^^^

    Here is how to use Picture::

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

    which produces the following Latex output::

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


    Example: Two Figures in multicol Environment 
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Here is the code to add two figures to a multicol environment. Note that 
    the `float` package needed to be added to allow figures to be added to 
    the multicol environment. If the `float` package is omitted then latex 
    will issue an error such as `Package multicol Warning: Floats and 
    marginpars not allowed inside multicols environment!` and then not include 
    the figures in the pdf output.::
    
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

    which produces the following Latex output::

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

    Example: maketitle
    ^^^^^^^^^^^^^^^^^^
    
    Here is how to add a title, author and date to the preamble::
    
        d = Document(   classname='report',
                        options=['9pt', 'twoside'])    

        d.add(Command('title', ['Document Title']))
        d.add(Command('author', ['Author Name']))
        d.add(Command('date', ['2016-02-29']))        
        d.add(Tag('maketitle'))
            
    which produces the following Latex output::  

        \\documentclass[9pt,twoside]{report}
        \\title{Document Title}
        \\author{Author Name}
        \\date{2016-02-29}
        \\begin{document}
        \\maketitle
        \\end{document}
        
"""


__author__ = "Barrett Edwards"
__maintainer__ = "Barrett Edwards"
__copyright__ = "Copyright 2016"
__license__ = "MIT"
__version__ = "0.1.0"
__email__ = "BarrettEdwardsOSS@gmail.com"
__status__ = "Development"


import os
import sys 
import tempfile
import string 
import random 
import subprocess 
import argparse
import shutil


_UNICODE_TO_LATEX_MAPPING = {
                            u"\u0020":" ",
                            u"\u0023":"\\#",
                            u"\u00A0":" ",
                            u"\u00A2":"{\\textcent}",
                            u"\u00A3":"{\\textsterling}",
                            u"\u00A9":"{\\textcopyright}",
                            u"\u00AE":"{\\textregistered}",
                            u"\u00B0":"{\\textdegree}",
                            u"\u2011":"{\\textendash}",
                            u"\u2013":"{\\textendash}",
                            u"\u2014":"{\\textemdash}",
                            u"\u2015":"{\\textemdash}",
                            u"\u2018":"`",
                            u"\u2019":"'",
                            u"\u201C":"{\\textquotedblleft}",
                            u"\u201D":"{\\textquotedblright}",
                            u"\u2026":"{\\ldots}",
                            u"\u202F":" ",
                            u"&amp;":"\\&",
                            u"&":"\\&",
                            u"$":"\\$",
                            u"\u0391":"$\\Alpha$",
                            u"\u0392":"$\\Beta$",
                            u"\u0393":"$\\Gamma$",
                            u"\u0394":"$\\Delta$",
                            u"\u0395":"$\\Epsilon$",
                            u"\u0396":"$\\Zeta$",
                            u"\u0397":"$\\Eta$",
                            u"\u0398":"$\\Theta$",
                            u"\u0399":"$\\Iota$",
                            u"\u039A":"$\\Kappa$",
                            u"\u039B":"$\\Lambda$",
                            u"\u039E":"$\\Xi$",
                            u"\u039F":"${\\rm O}$",
                            u"\u03A0":"$\\Pi$",
                            u"\u03A1":"$\\Rho$",
                            u"\u03A3":"$\\Sigma$",
                            u"\u03A4":"$\\Tau$",
                            u"\u03A5":"$\\Upsilon$",
                            u"\u03A6":"$\\Phi$",
                            u"\u03A7":"$\\Chi$",
                            u"\u03A8":"$\\Psi$",
                            u"\u03A9":"$\\Omega$",
                            u"\u03AD":"$\\acute{\\epsilon}$",
                            u"\u03AE":"$\\acute{\\eta}$",
                            u"\u03AF":"$\\acute{\\iota}$",
                            u"\u03B0":"$\\acute{\\ddot{\\upsilon}}$",
                            u"\u03B1":"$\\alpha$",
                            u"\u03B2":"$\\beta$",
                            u"\u03B3":"$\\gamma$",
                            u"\u03B4":"$\\delta$",
                            u"\u03B5":"$\\epsilon$",
                            u"\u03B6":"$\\zeta$",
                            u"\u03B7":"$\\eta$",
                            u"\u03B8":"$\\texttheta$",
                            u"\u03B9":"$\\iota$",
                            u"\u03BA":"$\\kappa$",
                            u"\u03BB":"$\\lambda$",
                            u"\u03BC":"$\\mu$",
                            u"\u03BD":"$\\nu$",
                            u"\u03BE":"$\\xi$",
                            u"\u03BF":"${\\rm o}$",
                            u"\u03C0":"$\\pi$",
                            u"\u03C1":"$\\rho$",
                            u"\u03C2":"$\\varsigma$",
                            u"\u03C3":"$\\sigma$",
                            u"\u03C4":"$\\tau$",
                            u"\u03C5":"$\\upsilon$",
                            u"\u03C6":"$\\varphi$",
                            u"\u03C7":"$\\chi$",
                            u"\u03C8":"$\\psi$",
                            u"\u03C9":"$\\omega$",
                            u"\uFB01":"fi",
                            u"\uFB02":"fl"
                            }
"""A global dictionary used to substitute special unicode characters into latex character commands"""

def unicode_to_latex(unicode_str):
    """Module function to convert unicode strings into properly escaped Latex safe strings
    
    Args:
        unicode_str (str): String to convert from unicode to a latex safe 
                           command string
    
    Returns:
        unicode_str (str): A string that has been converted to latex 
    """

    # Post process some unicode characters into latex symbols
    keys = _UNICODE_TO_LATEX_MAPPING.keys()
    for k in keys:
        unicode_str = unicode_str.replace(k,_UNICODE_TO_LATEX_MAPPING[k])

    return unicode_str


class NitrileError(Exception):
    """A Base class for all Nitrile Exceptions."""
    pass


class Document():
    """Class that represents a single Latex document

    This is the starting point for a Latex document.
    All document contents are added to this class.
    This class also includes the ability to build a tex and pdf 
    representation of the Latex document
    
    Args:
        classname (str): The type of Latex document to create
                         (e.g. article, book, etc)

        options (list): A list of strings to use as options to the Latex
                        document class. i.e. \documentclass[option1, option2]{classname}
    
    Latex Dependencies: 
        None: No special Latex packages required for this object
        
    """

    def __init__(   self,\
                    classname='article',\
                    options=[]\
                    ):        

        self.documentclass = _DocumentClass( classname=classname, \
                                             options=options)
        self.packages = []
        self.commands = []        
        self.body = []
        
        # need to include this for underlines that will break across lines
        # this pacakge is needed for Content()
        self.add(Package('ulem', options=['normalem']))


        return        
        
    def add(    self, 
                item):
        """Add an item to the `Document`
        
        This method is how all contents are added to the `Document`. 
        
        Args:
            item (`Package`, Command, Body, string): The item to be added.  
        
        Returns:
            item: Returns the object to be added for convenience 
        
        Raises:
            NitrileError: If item is not a `Package`, Command, Body, or string object

        """        
        
        if isinstance(item, Package):
            self.packages.append(item)
        elif isinstance(item, Command):
            self.commands.append(item)
        elif isinstance(item, Body):
            self.body.append(item)
        elif isinstance(item, basestring):
            self.body.append(Content(item))
        else:
            msg = 'Attempted to add unsupported object to document'
            raise NitrileError(msg)
    
        return item
        
    def pdf(    self, 
                filename=None, 
                force=False, 
                open_when_done=False):
        """Convert Document into a PDF file
        
        When called, this method will convert all the Document contents into
        a single string representing a Latex document, write that string out to
        a .tex file in a temporary directory, and build the .tex file into a pdf
        file using the pdflatex command line program. 
        
        If a filepath is provided, the PDF will be moved and renamed to that 
        filepath location. If no filepath is provided, then the resulting PDF
        will be opened by the default PDF reader application for the user to
        review or save to a new location. 
        
        Args:
            filename (string): The filename for the output PDF file. This can
                               be a relative or absolute directory name 
                               (./path/to/dir/, or /path/to/dir/), a filename
                               (output.pdf) or a relative or absolute filepath
                               (./path/to/dir/output.pdf or
                               /path/to/dir/output.pdf)
            
            force (bool): If true, any existing output file collision will be
                          overwritten. Default is to not overwrite any existing
                          file in the file system.
            
            open_when_done (bool): If true, will cause the resulting PDF file
                                   to be opened by the default application. 
            
        """
                        
        # STEPS:
        # 1. generate tex string
        # 2. create temporary directory (needed because pdflatex needs a real
        #    directory to put temp files)
        # 3. generate output filename
        # 4. write out tex string to file in temp directory
        # 5. run pdflatex twice to generate pdf
        # 6. remove build files
        # 7. move the PDF file to the requested location
        # 8. open PDF file if needed
        # 9. destroy temp directory
        
        # STEP 1
        # generate the entire tex file string
        tex = self.tex()
                
        # STEP 2
        # Create temporary directory
        temp_dirpath = tempfile.mkdtemp()
                
        # STEP 3
        # Generate build process filenames using a random name  
        char_set = string.ascii_lowercase + string.digits
        random_filename = ''.join(random.choice(char_set) for _ in range(10))
        tex_filename = random_filename + '.tex'
        pdf_filename = random_filename + '.pdf'
        tex_filepath = os.path.join(temp_dirpath, tex_filename)
        pdf_filepath = os.path.join(temp_dirpath, pdf_filename)
                
        # STEP 4
        # write out tex string to file in temp directory        
        with open(tex_filepath, 'w') as fp:
            fp.write(tex.encode('utf8'))
                
        # STEP 5
        # run pdflatex twice to generate pdf
        cmd = [ 'pdflatex','--shell-escape', '--halt-on-error', \
                '-output-directory', temp_dirpath, tex_filepath]
        try:
            rv = subprocess.check_output(cmd)
        except subprocess.CalledProcessError as e:
            print "PDF build failed: " + tex_filepath + " Return Code: " + \
                    str(e.returncode) + " Error Message: " + str(e.output)

        # run build a second time to resolve all labels
        try:
            rv = subprocess.check_output(cmd)
        except subprocess.CalledProcessError as e:
            print "PDF build failed: " + tex_filepath + " Return Code: " + \
                    str(e.returncode) + " Error Message: " + str(e.output)
                
        # STEP 6
        # remove the build files
        for f in os.listdir(temp_dirpath):
            if f.endswith('.log') or f.endswith('.aux') or f.endswith('.gz'):
                os.remove(os.path.join(temp_dirpath,f))
                
        # STEP 7
        # move the PDF file to the requested location, if requested 
        # if specified filepath is a directory, use the random file name for 
        # destination PDF name
        # if sepcified filepath is a file name, check if it exists before 
        # overwriting
        # if file already exists, check force parameter before overwriting
        if filename is not None:
            filepath = os.path.expanduser(filename)
            if os.path.isdir(filepath):
                src = pdf_filepath
                dst = os.path.join(filepath,pdf_filename)
                
                if os.path.exists(dst) and force is False:
                    print "Error: Cannot move PDF file to requested location. '\
                          'File already exists: " + dst
                else:
                    shutil.move(src,dst)
                    pdf_filepath = dst 
            else:
                src = pdf_filepath
                dst = os.path.expanduser(filepath)
            
                if os.path.exists(dst) and force is False:
                    print "Error: Cannot move PDF file to requested location. '\
                          'File already exists: " + dst
                else:
                    shutil.move(src,dst)
                    pdf_filepath = dst       
                
        # STEP 8
        # Open the PDF if requested
        if open_when_done:
            if sys.platform.startswith('darwin'):
                subprocess.call(('open', pdf_filepath))
            elif os.name == 'nt':
                os.startfile(pdf_filepath)
            elif os.name == 'posix':
                subprocess.call(('xdg-open', pdf_filepath))
                
        # STEP 9
        # remove temp directory        
        # stopped doing this because opening the PDF sometimes can't happen
        # fast enough and the file gets deleted before it can open
        # shutil.rmtree(temp_dirpath)
                        
        return  
    
    def tex(    self, 
                filename=None, 
                force=False, 
                open_when_done=False):
        """Convert Document into a latex string 
        
        When called, this method will convert all the Document contents into
        a single string representing a Latex document, and then if requested,
        write that string out to a .tex file in a temporary directory. This 
        function will not build the .tex file into a PDF. 
        
        If a filepath is provided, the resulting .tex file will be moved and
        renamed to that filepath location. If no filepath is provided, then 
        the resulting .tex file will be opened by the default .tex application
        for the user to review or save to a new location. 
        
        Args:
            filename (string): The filename for the output .tex file. This can
                               be a relative or absolute directory name
                               (./path/to/dir/, or /path/to/dir/), a filename
                               (output.tex) or a relative or absolute filepath
                               (./path/to/dir/output.tex or
                               /path/to/dir/output.tex)
            
            force (bool): If true, any existing output file collision will be
                          overwritten. Default is to not overwrite any existing
                          file in the file system.
            
            open_when_done (bool): If true, will cause the resulting .tex file
                                   to be opened by the default application. 
            
        Returns:
                : A unicode string as the latex representation
                  of the Document. 

        """
                    
        # STEPS
        # 1. Generate Preamble
        # 2. Start body
        # 3. Generate body
        # 4. Generate footer
        
        l = []
        
        # STEP 1: Generate Preamble
        # documentclass
        l.append(self.documentclass._tex())
        
        # append packages
        for p in self.packages:
            l.append(p._tex())
        
        # append commands 
        for c in self.commands:
            l.append(c._tex())
        
        # STEP 2: Begin body 
        l.append(u'\\begin{document}\n')
        
        # STEP 3: Generate Body
        for b in self.body:
            l.extend(b._tex())     
        
        # STEP 4: Generate footer
        l.append(u'\n\\end{document}')
        
        # Consolidate into a single string         
        tex = u''.join(l)
        
        # if a filename was passed then write out the tex to a file
        if filename is not None:
            filepath = os.path.expanduser(filename)
            if os.path.exists(filepath) and not force:
                print "Error: file exists:", filepath
            else:
                with open(filepath, 'w') as fp:
                    fp.write(tex.encode('utf8'))
                    
                if open_when_done:
                    if sys.platform.startswith('darwin'):
                        subprocess.call(('open', filepath))
                    elif os.name == 'nt':
                        os.startfile(filepath)
                    elif os.name == 'posix':
                        subprocess.call(('xdg-open', filepath))
        
        # if the user didn't pass a filename but wants to open the tex,
        # then write out the tex to a temp file and open it
        if filename is None and open_when_done:
            # create temp directory
            temp_dirpath = tempfile.mkdtemp()
            
            # generate random filename 
            char_set = string.ascii_lowercase + string.digits
            random_filename = ''.join(random.choice(char_set) for _ in range(10))
            tex_filename = random_filename + '.tex'
            filepath = os.path.join(temp_dirpath, tex_filename)
        
            # Write out the file
            with open(filepath, 'w') as fp:
                fp.write(tex.encode('utf8'))
        
            # open the file
            if sys.platform.startswith('darwin'):
                subprocess.call(('open', filepath))
            elif os.name == 'nt':
                os.startfile(filepath)
            elif os.name == 'posix':
                subprocess.call(('xdg-open', filepath))
        
        return tex


class _DocumentClass():
    """Class that represents the type of Latex document being created. 

    This class is used just once per Document to set what type of Latex 
    Document is being made. 
    
    This is an internal class and should not be seen by the user. It should
    only ever be called once by the Document constructor.
    
    Args:
        classname (str): The type of Latex document to create 
                         (e.g. article, report, book, etc)

        options (list): A list of strings to use as options to the Latex
                        document class. i.e.
                        \documentclass[option1, option2]{classname}
    
    Raises:
        NitrileError: Raises if requested document class isn't supported
    
    Latex Dependencies 
        None: No special Latex packages required for this object
        
    """
    def __init__(   self, 
                    classname, 
                    options=[]):
                    
        self.supported_classes = ['article', 'report', 'book', 'extreport',
                                  'extarticle']
        self.classname = classname
        self.options = options
        
        if classname not in self.supported_classes:
            msg = 'Requested document class ' + classname + \
                  ' not in list of supported types: ' + \
                  str(self.supported_classes)
            raise NitrileError(msg)
    
        return

    def _tex(self):
        """Converts this object and any child objects into an array of unicode
        strings in Latex formatting. 
        """
        
        s = u'\\documentclass[' + u','.join(self.options) + ']{' + \
            self.classname + '}\n'
        
        return s


class Package():
    """A class to represent a Latex package
    
    `Package` objects are used to add specific Latex packages to the Latex 
    Document preamble. A `Package` can be added to the `Document` at any time.
    The preamble list of latex packages will be built in the order that the 
    `Package` objects were added to the `Document`
    
    Args:
        name (string): The name of the Latex Package to be added
        
        options (list): A list of strings to include as the latex package 
                        options
    
    Latex Dependencies 
        None: No special Latex packages required for this object
        
    """    
    
    def __init__(   self, 
                    name, 
                    options=None):
                    
        self.name = name
        self.options = options
    
        return

    def _tex(self):
        """Converts this object and any child objects into an array of unicode
        strings in Latex formatting. 
        """
        
        s = u'\\usepackage'
        if self.options is not None:
            s += u'[' + u','.join(self.options) + u']'
        s = s + '{%s}\n' % self.name
        
        return s
        
        
class Command():
    """A class to represent a Latex command
    
    `Command` objects are used to add specific Latex commands to the Latex 
    Document preamble. A `Command` can be added to the `Document` at any time.
    The preamble list of latex commands will be built in the order that the 
    `Command` objects were added to the `Document`
    
    Args:
        name (string): The name of the Latex Command to be added
        
        options (list): A list of strings to include as the latex command 
                        options
    
    Latex Dependencies 
        None: No special Latex packages required for this object
            
    """
    
    def __init__(   self, 
                    name, 
                    options=[]):
                    
        self.name = name
        self.options = options
    
        return

    def _tex(self):
        """Converts this object and any child objects into an array of unicode
        strings in Latex formatting. 
        """
        
        s = u'\\' + self.name
        for o in self.options:
            s += '{' + o + '}'
        s += '\n'
        
        return s


class Body():
    """A base class for all Nitrile objects that represent Latex Body content.
    
    The content of the `Document` such as text, figures, sections, tables, etc 
    are all considered `Body` objects. All of these subclasses inherit from 
    `Body`. 
    
    A `Body` object can be added to the `Document` at any time. The final 
    Document output will be built in the order that the `Body` objects were
    added to the `Document`.
    
    This class is intended to be subclasses and is never instantiated 
    on its own.
    
    Args:
        None: This is a base class that doesn't have any content.
    
    Returns:
        item: Returns the object to be added for convenience
        
    Latex Dependencies 
        None: No special Latex packages required for this object
                
    """
    
    def __init__(self):
        
        self.body = []
        
        return
        
    def add(    self, 
                item):        
        """Add a child Body object to this Body object. 
            
        The add function is a common action among all subclasses so it is 
        implemented here in the base Body class for all subclasses to use. 
            
        Args:
            item (Body, string): A Body subclass such as a Content,
                                 Environment, Table, Section, Figure, List,
                                 Picture to add as a child object of this Body
                                 object. If a string is passed, it is first
                                 converted into a Content object and then added
                                 as a child.
            
        Raises:
            NitrileError: Raises if item is not a Body subclass or a string
                          (which is converted into a Content object) 

        """
                
        if isinstance(item, Body):
            self.body.append(item)
        elif isinstance(item, basestring):
            self.body.append(Content(item))
        else:
            msg = 'Attempted to add unsupported object to Body object'
            raise NitrileError(msg)
    
        return item


class Content(Body):
    """A class to hold generic text content.
    
    A `Content` object is used to hold generic text. The class supports minor
    formatting options such as bold and italic. 
    
    By default, when a `Content` object is created, the text passed in is 
    converted from unicode to Latex safe text. This implies that any special 
    characters such as $ or \\\ or other special unicode characters will be 
    properly escaped. 
    
    A `Content` object can also be used to add native Latex formatting tags
    such as a \\newpage command or a $math$ section by setting the `convert`
    parameter to `False`. 
    
    Args:
        content (str): This is the text to add to the `Document`
        
        convert (bool): If true, properly convert passed in text to use Latex
                        safe escape sequences. For example, a $math$ segment is
                        converted into \\\\$math\\\\$.
        
        bold (bool): If true, cause passed in text to be bolded.
        
        italic (bool): If true, cause passed in text to be italicized.

        underline (bool): If true, cause passed in text to be underlined.
        
        prenewlines (int): Number of newlines to prefix this Content
        
        postnewlines (int): Number of newlines to suffix this Content
        
        noindent (bool): If true, add a \\\\noindent tag before Content
        
        flatten (bool): If true, all children objects will be flattened into a 
                        single string with this objects content instead of 
                        being returned as multiple strings
    
    Latex Dependencies 
        None: No special Latex packages required for this object
                
    """
    
    def __init__(   self, 
                    content, 
                    convert=True, 
                    bold=False, 
                    italic=False,
                    underline=False,
                    prenewlines=0,
                    postnewlines=0,
                    noindent=False,
                    flatten=False):
                    
        # call parent class constructor
        Body.__init__(self)
        
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.prenewlines = prenewlines
        self.postnewlines = postnewlines
        self.noindent = noindent
        self.flatten = flatten
                
        # convert passed in text into latex safe escape sequences
        if convert:
            self.content = unicode_to_latex(content)
        else:
            self.content = content
        
        return            
    
    def _tex(self):
        """Converts this object and any child objects into an array of unicode
        strings in Latex formatting. 
        """
        
        l = []
        
        for i in range(self.prenewlines):
            l.append('\n')
        
        if self.noindent:
            l.append('\\noindent ')
        
        if self.underline:
            l.append('\\uline{')

        if self.bold:
            l.append('\\begin{bf}')
        
        if self.italic:
            l.append('\\begin{em}')
                
        # If we want to flatten all children,
        # then get a list of all the children strings, join them, and then 
        # just append them to the self.content string 
        if self.flatten:
            sublist = []
            for b in self.body:
                sublist.extend(b._tex())                
            l.append(self.content + ''.join(sublist))

        else:
            # If we are not flattening the children,
            # just add the self content as a list item
            # and then add the middle content as seperate list items
            l.append(self.content)
        
            # add middle content 
            for b in self.body:
                l.extend(b._tex())

        if self.italic:
            l.append('\\end{em}')
        
        if self.bold:
            l.append('\\end{bf}')

        if self.underline:
            l.append('}')

        for i in range(self.postnewlines):
            l.append('\n')
        
        return l


class Tag(Body):
    """A class to represent generic Latex Tag.
    
    A `Tag` object is used to represent a general Latex tag such as \\newline 
    or \\maketitle. The Tag object will properly escape with the correct 
    number of backslashes in the output tex. The Tag object is mainly for 
    code convenience so the user doesn't have to constantly remember to add 
    extra backslashes to properly escape tags. 
    
    The Tag generates tex content similar to the following::
        
        \\name{options}
        
    Args:
        name (str): This is the name of the tag
        
        options (list): List of strings to paste into options field in Latex 
                       \\\\name{option1}{option2}
                       
        prenewlines (int): Number of newlines to prefix this Tag
        
        postnewlines (int): Number of newlines to suffix this Tag
    
    Latex Dependencies 
        None: No special Latex packages required for this object
            
    """
    
    def __init__(   self, 
                    name, 
                    options=[],
                    prenewlines=0,
                    postnewlines=0):
                    
        # call parent class constructor
        Body.__init__(self)
        
        self.prenewlines = prenewlines
        self.postnewlines = postnewlines
        self.name = name
        self.options = options
        
        return    
    
    def _tex(self):
        """Converts this object and any child objects into an array of unicode
        strings in Latex formatting. 
        """
        
        l = []
        
        for i in range(self.prenewlines):
            l.append('\n')
        
        # Begin the environment
        tag = u'\\' + self.name 
        for o in self.options:
            tag += '{' + o + '}'
        l.append(tag)
        
        for i in range(self.postnewlines):
            l.append('\n')
    
        # add middle content 
        for b in self.body:
            l.extend(b._tex())
    
        return l
        
        
class Environment(Body):
    """A class to represent generic Latex Environment.
    
    An `Environment` object is used to represent a Latex environment such as 
    `minipage` where subcontent is added within the Environment. 
    
    The `name` passed in is simply pasted into a basic environment framework
    as shown below:: 
    
        \\begin{name}{options}
        <sub content>
        \\end{name} 
        
    Args:
        name (str): This is the name of the environment
        
        options (str): string to paste into options field in Latex 
                       begin{name}{options} tag
            
        tight (bool): If true, shrink the space between lines
    
    Latex Dependencies 
        None: No special Latex packages required for this object
            
    """
    
    def __init__(   self, 
                    name, 
                    options=[],
                    tight=False):
                    
        # call parent class constructor
        Body.__init__(self)
        
        self.name = name
        self.options = options
        self.tight = tight
        
        return    
    
    def _tex(self):
        """Converts this object and any child objects into an array of unicode
        strings in Latex formatting. 
        """
        
        l = []
        
        # Begin the environment
        tag = '\n\\begin{' + self.name + '}' 
        for o in self.options:
            tag += '{' + o + '}'
        
        if self.tight:
            tag += '\setlength{\parskip}{0cm} '    
            
        tag += '\n'    
        l.append(tag)
            
        # add middle content 
        for b in self.body:
            l.extend(b._tex())
            
        # end the environment 
        end = '\n\\end{' + self.name + '}\n'
        l.append(end)

        return l


class Chapter(Body):
    """A class to represent a Chapter in Latex
    
    A Chapter will create a \\\\chapter{} in the Latex document. All content
    within the Latex Chapter should be added to this class object 
    
    Args:
        title (string): A string to represent the heading of the Latex Chapter. 
        
        numbered (bool): If true, the Latex Chapter will be numbered in the 
                         table of contents. If false, the Latex Chapter will be
                         un-numbered (i.e. \\\\chapter*{})
        
        label (string): The Latex label name to give this chapter to be used 
                        by \\\\ref{} tags elsewhere in the document

        clearpage (bool): If true, a \\\\clearpage tag will be added prior to 
                          the Chapter
                        
        cleardoublepage (bool): If true, a \\\\cleardoublepage tag will be
                                added prior to the Chapter

    Latex Dependencies 
        classanme (Mandatory): The classname for the Latex document must be 
        `report` and cannot be `article` because `articles` don't have 
        chapters. 

    """
    
    def __init__(   self, 
                    title, 
                    numbered=False, 
                    label=None, 
                    clearpage=False,
                    cleardoublepage=False):
                    
        # call parent class constructor
        Body.__init__(self)
        
        self.title = unicode_to_latex(title)
        self.clearpage = clearpage
        self.cleardoublepage = cleardoublepage
        self.numbered = numbered
        self.label = label
        self.type = 'chapter'
        
        return
        
    def _tex(self):
        """Converts this object and any child objects into an array of unicode
        strings in Latex formatting. 
        """
        
        l = []
        
        l.append('\n')
        
        if self.cleardoublepage:
            l.append('\\cleardoublepage\n')            
        elif self.clearpage:
            l.append('\\clearpage\n')
        
        l.append('\\' + self.type)
        
        if self.numbered is False:
            l.append('*')
        
        l.append('{' + self.title + '}')
        
        if self.label:
            l.append('\\label{' + self.label + '}\n')
            
        # add middle content 
        for b in self.body:
            l.extend(b._tex())
            
        return l            
        
        
class Section(Chapter):
    """A class to represent a Section in Latex
    
    A Section will create a \\\\Section{} in the Latex document. All content
    within the Latex Section should be added to this class object 
    
    Args:
        title (string): A string to represent the heading of the Latex Section. 
        
        numbered (bool): If true, the Latex section will be numbered in the 
                         table of contents. If false, the Latex section will be
                         un-numbered (i.e. \\\\section*{})
        
        label (string): The Latex label name to give this section to be used 
                        by \\\\ref{} tags elsewhere in the document

        clearpage (bool): If true, a \\\\clearpage tag will be added prior to 
                          the Chapter
                                                  
        cleardoublepage (bool): If true, a \\\\cleardoublepage tag will be
                                added prior to the Section

    Latex Dependencies 
        None: No special Latex packages required for this object

    """
    
    def __init__(   self, 
                    title, 
                    numbered=False, 
                    label=None, 
                    clearpage=False,
                    cleardoublepage=False):
                    
        # call parent class constructor
        Chapter.__init__(    self, 
                             title, 
                             numbered=numbered, 
                             label=label, 
                             clearpage=clearpage,
                             cleardoublepage=cleardoublepage)

        self.type = 'section'
        
        return          
        
        
class SubSection(Chapter):
    """A class to represent a SubSection in Latex
    
    A Section will create a \\\\SubSection{} in the Latex document. All content
    within the Latex SubSection should be added to this class object 
    
    Args:
        title (string): A string to represent the heading of the Latex 
                        SubSection.
        
        numbered (bool): If true, the Latex SubSection will be numbered in the
                         table of contents. If false, the Latex SubSection will
                         be un-numbered (i.e. \\\\subsection*{})
        
        label (string): The Latex label name to give this SubSection to be used
                        by \\\\ref{} tags elsewhere in the document

        clearpage (bool): If true, a \\\\clearpage tag will be added prior to 
                          the Chapter
                                                  
        cleardoublepage (bool): If true, a \\\\cleardoublepage tag will be
                                added prior to the SubSection            

    Latex Dependencies 
        None: No special Latex packages required for this object
        
    """
    
    def __init__(   self, 
                    title, 
                    numbered=False, 
                    label=None, 
                    clearpage=False,
                    cleardoublepage=False):        

        # call parent class constructor
        Chapter.__init__(    self, 
                             title, 
                             numbered=numbered, 
                             label=label, 
                             clearpage=clearpage,
                             cleardoublepage=cleardoublepage)

        self.type = 'subsection'
        
        return


class SubSubSection(Chapter):
    """A class to represent a SubSubSection in Latex
    
    A Section will create a \\\\SubSubSection{} in the Latex document. All 
    content within the Latex SubSubSection should be added to this class object
    
    Args:
        title (string): A string to represent the heading of the Latex 
                        SubSubSection.
        
        numbered (bool): If true, the Latex SubSubSection will be numbered in
                         the table of contents. If false, the Latex 
                         SubSubSection will be un-numbered
                         (i.e. \\\\sububsection*{}) 
        
        label (string): The Latex label name to give this SubSubSection to be
                        used by \\\\ref{} tags elsewhere in the document

        clearpage (bool): If true, a \\\\clearpage tag will be added prior to 
                          the Chapter
                                                  
        cleardoublepage (bool): If true, a \\\\cleardoublepage tag will be
                                added prior to the SubSubSection            

    Latex Dependencies 
        None: No special Latex packages required for this object
        
    """
    
    def __init__(   self, 
                    title, 
                    numbered=False, 
                    label=None, 
                    clearpage=False,
                    cleardoublepage=False):
        
        # call parent class constructor
        Chapter.__init__(    self, 
                             title, 
                             numbered=numbered, 
                             label=label, 
                             clearpage=clearpage,
                             cleardoublepage=cleardoublepage)

        self.type = 'subsubsection'
        
        return
        
        
class _List(Body):
    """A class to represent a bulleted list in Latex
    
    A List will create a \\\\begin{itemize} tag in the Latex document. All
    list bullet items should be added as a child to this object
    
    This object is a private class that is intended to be subclassed and should
    not be directly instanced by the user
    
    Args:
        tight (bool): If true, predefined measurements will be used to form a
                      tighter spaced list

    Latex Dependencies 
        None: No special Latex packages required for this object
        
    """
    
    def __init__(   self,
                    tight=False):
                    
        # call parent class constructor
        Body.__init__(self)
        
        self.type = 'itemize'
        self.tight = tight
        
        return
        
    def _tex(self):
        """Converts this object and any child objects into an array of unicode
        strings in Latex formatting. 
        """
        
        l = []
        
        # Begin the environment
        header = '\n\\begin{' + self.type + '}' 
        
        if self.tight:
            header += ' \\setlength{\\itemsep}{0cm}'\
                      ' \\setlength{\\parskip}{0cm}'
        
        header += '\n'
        
        l.append(header)
    
        # add middle content 
        for b in self.body:
            l.append('\\item ' + ''.join(b._tex()) + '\n')
        
        # end the environment 
        footer = '\\end{' + self.type + '}\n'
        l.append(footer)

        return l    


class Itemize(_List):
    """A class to represent an un-numbered bulleted list in Latex
    
    An Itemize object will create a \\\\begin{itemize} tag in the Latex
    document. All list bullet items should be added as a child to this object
    
    Args:
        tight (bool): If true, predefined measurements will be used to form a
                      tighter spaced list

    Latex Dependencies 
        None: No special Latex packages required for this object
        
    """
    
    def __init__(   self, 
                    tight=False):     
                       
        # call parent class constructor
        _List.__init__(  self,
                        tight)
                        
        self.type = 'itemize'

        return


class Enumerate(_List):
    """A class to represent a numbered bulleted list in Latex
    
    An Enumerate object will create a \\\\begin{enumerate} tag in the Latex
    document. All list bullet items should be added as a child to this object
    
    Args:
        tight (bool): If true, predefined measurements will be used to form a
                      tighter spaced list

    Latex Dependencies 
        None: No special Latex packages required for this object
        
    """
    
    def __init__(   self, 
                    tight=False):      
                      
        # call parent class constructor
        _List.__init__(  self, 
                        tight)
                        
        self.type = 'enumerate'
        
        return
        
    
class Table(Body):
    """A class to represent a Table in Latex
    
    A Table object will create a \\\\begin{tabularx} tag in Latex. The 
    columnparameters string is the single configuration string to set the 
    widths and settings for each column. 
    
    All table Row objects should be added as children to this object. 
    
    The explanations for the possible columnparameters are shown below:
    
    =========   ===============================================================
    Parameter   Explanation 
    =========   ===============================================================
    L           Left justified text with a variable column width
    C           Center justified text with a variable column width
    R           Right justified text with a variable column width
    l           Left justified text with column width just wide enough for the 
                text
    c           Center justified text with column width just wide enough for 
                the text
    r           Right justified text with column width just wide enough for 
                the text
    \|          Pipe will add a vertical border at that location    
    @\{\}       This will remove any space between two columns. | L @\{\} R |
                will produce a two column table but there will be no space 
                between the two.     
    =========   ===============================================================
    
    Args:
        columnparameters (str): A string is the single configuration string to
                                set the widths and settings for each column.
                                e.g. '| L | C | r | 
    Latex Dependencies
        tabularx (Mandatory): Latex package needed for table generation. 
                              Use Package('tabularx')

    """
    
    def __init__(   self, 
                    columnparameters):
                    
        # call parent class constructor
        Body.__init__(self)
        
        self.columnparameters = columnparameters
        
        return

    def _tex(self):
        """Converts this object and any child objects into an array of unicode
        strings in Latex formatting. 
        """
              
        l = []
        
        # replace custom column parameters with tabular X syntax        
        columnparameters = self.columnparameters\
                .replace('L', '>{\\raggedright\\arraybackslash}X')\
                .replace('R', '>{\\raggedleft\\arraybackslash}X')\
                .replace('C', '>{\\centering\\arraybackslash}X')
                
        # Begin the environment
        header = '\n\n\\noindent \\begin{tabularx} {\\columnwidth}{' + \
                 columnparameters + '}\n'
        l.append(header)

        # add the rows 
        numrows = len(self.body)
        for i,r in enumerate(self.body):
            l.extend(r._tex())
            if i < (numrows - 1):
                l.append('\n')            
        
        # end the environment 
        footer = '\n \\end{tabularx} \n'
        l.append(footer)

        return l    


class Row(Body):
    """A class to represent a Table Row in Latex
    
    A Row object must be added as a child to a Table object. The Row object
    is just a container that holds multiple child Body objects where each Body
    object is a different column of the Row. 
    
    Args:
        None
    
    Latex Dependencies 
        tabularx (Mandatory): Latex package needed for table generation. 
                              Use Package('tabularx')
        
    """
    
    def __init__(self):
        
        # call parent class constructor
        Body.__init__(self)
        
        return
        
    def _tex(self):
        """Converts this object and any child objects into an array of unicode
        strings in Latex formatting. 
        """
        
        l = []
        
        # add the columns  
        numcolumns = len(self.body)
        for i,c in enumerate(self.body):
            l.extend(c._tex())
            if i < (numcolumns - 1):
                l.append(' & ')
            else:
                l.append(' \\\\')
                
        return l


class Figure(Body):
    """A class to represent a Figure in Latex
    
    A Figure object will create a \\\\begin{figure} tag in Latex. 
    
    Args:
        imagefilename (str): A string specifying the filename for the Figure
                             image
                             
        width (str): A string specifying the width of the figure. This is latex
                     style tags such as \\\\columnwidth
        
        star (bool): If true, the figure tag will be changed to 
                     \\\\begin{figure*} which will span multiple text columns
        
        placement (str): The placement string to tell Latex where to put the
                         figure (i.e. 'htb')
        
        center (bool): If true, the \\\\centering tag will be added to the 
                       figure to center the figure in the environment
                       
        caption (str): The caption string to put beneath the figure
        
        label (str): The Latex label name to give this Figure to be
                     used by \\\\ref{} tags elsewhere in the document

    Latex Dependencies
        graphicx (Mandatory): Latex package required for figures. 
                              Use Package('graphicx')
        
        float (Optional): The float Latex package is only needed if a figure 
                          will span multiple columns (i.e. the Figure star 
                          parameter is True)
        
    """
    
    def __init__(   self, 
                    imagefilename=None, 
                    width='\\columnwidth', 
                    star=False, 
                    placement='htb', 
                    center=True, 
                    caption=None, 
                    label=None):
                    
        # call parent class constructor
        Body.__init__(self)

        self.placement = placement

        if imagefilename is not None:
            self.image = os.path.join(os.getcwd(),imagefilename)
        else:
            self.image = None
            
        self.width = width
        self.center = center
        self.caption = caption
        self.label = label
        self.star = star
        
        return
        
    def _tex(self):
        """Converts this object and any child objects into an array of unicode
        strings in Latex formatting. 
        """
        
        l = []
        
        if self.star:
            star = '*'
        else:
            star = ''
            
        # Begin the environment
        l.append('\n\\begin{figure' + star + '}[' + self.placement + ']\n')

        if self.center:
            l.append('\\begin{center}\n')    
        
        if self.image is not None:
            l.append(   '\\includegraphics[width=' + \
                        self.width + \
                        ']{' + \
                        self.image + \
                        '}\\\\')    
        
        # add potential drawing instructions
        for b in self.body:
            l.extend(b._tex())
            
        if self.center:
            l.append('\\end{center}\n')    
            
        if self.caption is not None:
            l.append('\\caption{' + self.caption + '}\n')    

        if self.label is not None:
            l.append('\\label{' + self.label + '}\n')    
        
        # end the environment 
        l.append('\\end{figure' + star + '}\n')

        return l   


class SubFigure(Body):
    """A class to represent a SubFigure in Latex
    
    A SubFigure object will create a \\\\begin{subfigure} tag in Latex. 
    
    Args:
        imagefilename (str): A string specifying the filename for the Figure
                             image

        subfigurewidth (str): A string specifying the width of the subfigure
                              within the figure. This is latex style tags such as 
                              0.5\\\\columnwidth        
                             
        imagewidth (str): A string specifying the width of the image within 
                          the figure. This is latex style tags such as 
                          \\\\columnwidth        
        
        placement (str): The placement string to tell Latex where to put the
                         figure (i.e. 'htb')
        
        center (bool): If true, the \\\\centering tag will be added to the 
                       figure to center the figure in the environment
                       
        caption (str): The caption string to put beneath the figure
        
        label (str): The Latex label name to give this Figure to be
                     used by \\\\ref{} tags elsewhere in the document

    Latex Dependencies
        graphicx (Mandatory): Latex package required for figures. 
                              Use Package('graphicx')
        
        subcaption (Mandatory): Latex package required for subfigures. 
                                Use Package('subcaption')

        float (Optional): The float Latex package is only needed if a figure 
                          will span multiple columns (i.e. the Figure star 
                          parameter is True)
    """
    
    def __init__(   self, 
                    imagefilename=None, 
                    subfigurewidth='0.5\\textwidth', 
                    imagewidth='\\textwidth', 
                    placement='htb', 
                    center=True, 
                    caption=None, 
                    label=None):
                    
        # call parent class constructor
        Body.__init__(self)
        
        if imagefilename is not None:
            self.image = os.path.join(os.getcwd(),imagefilename)
        else:
            self.image = None

        self.placement = placement
        self.subfigurewidth = subfigurewidth
        self.imagewidth = imagewidth
        self.center = center
        self.caption = caption
        self.label = label
        
        return
                
    def _tex(self):
        """Converts this object and any child objects into an array of unicode
        strings in Latex formatting. 
        """
        
        l = []
        
        # Begin the environment
        l.append(   '\\begin{subfigure}[' + \
                    self.placement + \
                    ']{' + \
                    self.subfigurewidth + \
                    '}\n')

        if self.center:
            l.append('\\centering\n')    
        
        if self.image is not None:    
            l.append(   '\\includegraphics[width=' + \
                        self.imagewidth + \
                        ']{' + \
                        self.image + \
                        '}\\\\')
        
        # add potential drawing instructions
        for b in self.body:
            l.extend(b._tex())
            
        if self.caption is not None:
            l.append('\n\\caption{' + self.caption + '}')    

        if self.label is not None:
            l.append('\n\\label{' + self.label + '}')    
        
        # end the environment 
        l.append('\n\\end{subfigure}\n')
        
        return l  


class Picture(Body):
    """A class to represent a Picture in Latex
    
    A Picture object will create a \\\\begin{picture} tag within a 
    \\\\begin{figure} environment in Latex. 
    
    Args:
        width (str): A string specifying the width of the picture. This is latex
                     style tags such as \\\\columnwidth

        height (str): A string specifying the height of the picture. This is latex
                      style tags such as \\\\columnwidth

        unitlength (str): A string specifying the standard unit length of 
                          drawing commands (i.e. draw a line 1 unit length 
                          long)        
        
        placement (str): The placement string to tell Latex where to put the
                         Figure (i.e. 'htb')
        
        center (bool): If true, the \\\\centering tag will be added to the 
                       figure to center the Picture in the Figure environment
                       
        caption (str): The caption string to put beneath the Figure
        
        label (str): The Latex label name to give this Figure to be
                     used by \\\\ref{} tags elsewhere in the document

        star (bool): If true, the figure tag will be changed to 
                     \\\\begin{figure*} which will span multiple text columns

    Latex Dependencies 
        None: No special Latex packages required for this object

    """
    
    def __init__(   self, 
                    width, 
                    height, 
                    unitlength=None, 
                    placement='htb', 
                    center=True, 
                    caption=None, 
                    label=None, 
                    star=False):
                    
        # call parent class constructor
        Body.__init__(self)
        
        self.unitlength = unitlength
        self.placement = placement
        self.center = center
        self.width = width
        self.height = height
        self.caption = caption
        self.label = label
        self.star = star
        
        return
        
    def _tex(self):
        """Converts this object and any child objects into an array of unicode
        strings in Latex formatting. 
        """
        
        l = []
        
        if self.unitlength is not None:
            l.append(   '\n\\setlength{\\unitlength}{' + \
                        self.unitlength + \
                        '}')
            
        if self.star:
            star = '*'
        else:
            star = ''  
            
        # Begin the environment
        l.append(   '\n\\begin{figure' + \
                    star + \
                    '}[' + \
                    self.placement + \
                    ']\n')

        if self.center:
            l.append('\\begin{center}\n')
            
        l.append(   '\\begin{picture' + \
                    star + \
                    '}(' + \
                    str(self.width) + \
                    ',' + \
                    str(self.height) + \
                    ')\n')
        
        # add potential drawing instructions
        for b in self.body:
            l.extend(b._tex())
                        
        # end the environment 
        l.append('\n\\end{picture' + star + '}')

        if self.caption is not None:
            l.append('\n\\caption{' + self.caption + '}')

        if self.center:
            l.append('\n\\end{center}')

        if self.label is not None:
            l.append('\n\\label{' + self.label + '}')  
        
        # end the environment 
        l.append('\n\\end{figure' + star + '}\n')        
        return l   


class SelfTest():
    """A class to perform tests on the Nitrile package
    
    Instantiating the SelfTest class does not perform any actions. To run the 
    tests, use the run() function which will parse CLI input parameters. 
    
    Args:
        None:

    """
    
    def __init__(self):
        
        self.args = None        
        self.tests = []
        self.tests.append(self._test_conference)
        self.tests.append(self._test_helloworld)
        self.tests.append(self._test_packages)        
        self.tests.append(self._test_commands)            
        self.tests.append(self._test_formatting)     
        self.tests.append(self._test_multicol)                     
        self.tests.append(self._test_quote)     
        self.tests.append(self._test_lists)
        self.tests.append(self._test_chapters)
        self.tests.append(self._test_sections)        
        self.tests.append(self._test_tables)        
        self.tests.append(self._test_figures)
        self.tests.append(self._test_subfigures)
        self.tests.append(self._test_pictures)
        self.tests.append(self._test_multicolfigure)
        self.tests.append(self._test_maketitle)
                
        return
        
    def _parser(self):
        """Function to parse CLI arguments"""
        
        desc = 'Nitrile Library Self Test'
        parser = argparse.ArgumentParser(description=desc)

        parser.add_argument(    '-n',
                                '--testnum',
                                required=False, 
                                action='store',
                                help='Test Num')
        
        parser.add_argument(    '-t',
                                '--tex',
                                required=False, 
                                action='store_true', 
                                help='Generate Tex')
                                
        parser.add_argument(    '-p',
                                '--pdf',
                                required=False,
                                action='store_true',
                                help='Generate PDF')
        
        parser.add_argument(    '-f',
                                '--filename',
                                required=False,
                                action='store',
                                help='File location for action')
                                
        parser.add_argument(    '-o',
                                '--open',
                                required=False,
                                action='store_true',
                                help='Open file when done')
                                
        parser.add_argument(    '-P',
                                '--print',
                                required=False,
                                action='store_true',
                                help='Print to screen')
                                
        parser.add_argument(    '--force',
                                required=False,
                                action='store_true',
                                help='Overwrite output file')
        
        parser.add_argument(    '-l',
                                '--list',
                                required=False,
                                action='store_true',
                                help='List available tests to run')
        
        self.args = vars(parser.parse_args())
        
        return        

    def run(self):
        """Run the self test application using CLI parameters"""
        
        # STEPS:
        # 1. run CLI parser
        # 2. Determine test num
        # 3. run requested actions
        # 4. Generate output files
        
        # STEP 1 
        # run CLI argument parser
        self._parser()
        
        # STEP 2 
        # determine test numebr to run
        # if the user didn't enter a number, default to 0
        # if the user did enter something, try and convert to an int
        if self.args['testnum'] is None:
            self.args['testnum'] = 1 
        else: 
            try: 
                self.args['testnum'] = int(self.args['testnum'])
            except ValueError as e: 
                print 'Error: Invalid test num. '\
                      'Entry must be a number' + \
                      e.message
                quit()
        
        if self.args['testnum'] > (len(self.tests)-1):
            print "Error: Requested test num is out of range. '\
                  'Num available tests: " + \
                  str(len(self.tests))
            quit()
        
        if self.args['list']:
            print 'Available tests:'
            for i,t in enumerate(self.tests):
                print str(i) + ": " + str(t.__name__)[6:]
            
            quit()
                
        # STEP 3
        # run requested actions
        test_num = self.args['testnum']
        test_function = self.tests[test_num]
        d = test_function()
                
        # STEP 4 
        # Generate output files 
        # generate tex file
        if self.args['tex']:
            tex = d.tex(    filename=self.args['filename'], 
                            open_when_done=self.args['open'], 
                            force=self.args['force'])
        
            if self.args['print']:
                print tex
                
        # generate PDF
        if self.args['pdf']:
            d.pdf(  filename=self.args['filename'], 
                    open_when_done=self.args['open'], 
                    force=self.args['force'])
                            
        return 
        
    def _test_conference(self):
        """Example code for conference proceedings"""

        d = Document(   classname='report',
                        options=['9pt', 'twoside'])
                        
        d.add(Package('titlesec'))
        d.add(Package('multicol')) 
        d.add(Package('extsizes'))
        d.add(Package('endnotes')) 
        d.add(Package('underscore')) 
        d.add(Package('changepage')) 
        d.add(Package('textcomp')) 
        d.add(Package('inputenc', options=['utf8x']))
        d.add(Package('tabularx')) 
        d.add(Package('DejaVuSansMono'))
        d.add(Package('graphicx'))
        d.add(Package('float'))
        d.add(Package('caption'))
        d.add(Package('subcaption'))
        
        d.add(Command('pagestyle', ['plain']))
        d.add(Command('renewcommand', ['\\chaptername', '']))
        d.add(Command('newcounter', ['readblockcounter']))
        d.add(Command('setcounter', ['readblockcounter','1']))

        cmd = '\\noindent \\mbox{\\bf (\\thereadblockcounter)} '\
                '\\stepcounter{readblockcounter}'
        d.add(Command('newcommand', ['\\readblock', cmd])) 

        d.add(Command('setlength', ['\\hoffset','-0.5 in']))
        d.add(Command('setlength', ['\\oddsidemargin','0 in']))
        d.add(Command('setlength', ['\\evensidemargin','0 in'])) 
        d.add(Command('setlength', ['\\textwidth','7.5 in']))
        d.add(Command('setlength', ['\\columnsep','.15in']))
        d.add(Command('setlength', ['\\voffset','-0.5 in']))
        d.add(Command('setlength', ['\\topmargin','0 in']))
        d.add(Command('setlength', ['\\headheight','0 in']))
        d.add(Command('setlength', ['\\headsep','0 in']))
        d.add(Command('setlength', ['\\textheight','9.7 in']))
        d.add(Command('setlength', ['\\footskip','0.3 in']))
    
        s = d.add(Section('\\vspace{-.2in} \\huge \\center Title \\\\ '
                          '\\vspace{2mm} \\small Author Name \\\\ '
                          '\\vspace{1mm} Author Title \\\\ '
                          '\\vspace{1mm} \\footnotesize Event Name '
                          '\\vspace{-6mm}', 
                          cleardoublepage=True, 
                          label='1', 
                          numbered=False))
    
        return d     

    def _test_helloworld(self):
        """Example code for Hello World"""

        d = Document(   classname='report',
                        options=['9pt', 'twoside'])
                        
        d.add("Hello, World!")   
        
        return d
    
    def _test_packages(self):
        """Example code to use Latex preamble Packages"""

        d = Document(   classname='report',
                        options=['9pt', 'twoside'])

        d.add(Package('DejaVuSansMono'))
        d.add(Package('inputenc', options=['utf8x']))
        
        d.add("Hello, World!")
                            
        return d
            
    def _test_commands(self):
        """Example code to show use of Latex preamble commands"""

        d = Document(   classname='report',
                        options=['9pt', 'twoside'])

        d.add(Command('pagestyle', ['plain']))
        d.add(Command('setlength', ['\\hoffset','-0.5 in']))        
        d.add("Hello, World!")
                            
        return d 
            
    def _test_formatting(self):
        """Example code to show use of text formatting"""

        d = Document(   classname='report',
                        options=['9pt', 'twoside'])

        d.add(Content('$\int_{a}^{b} x^2 dx$', 
                      convert=False, 
                      postnewlines=2))
                      
        d.add(Content('This content should be bold.', 
                      bold=True, 
                      postnewlines=2))
                      
        d.add(Content('This content should be italic.', 
                      italic=True, 
                      postnewlines=2))

        d.add(Content('This content should be underlined.', 
                      underline=True, 
                      postnewlines=2))

                            
        return d 
            
    def _test_multicol(self):
        """Example code to show use of multicol environment"""

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
                            
        return d 
            
    def _test_quote(self):
        """Example code to show use of a Quote Environment"""

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
                            
        return d 
        
    def _test_lists(self):
        """Example code to show use of Lists"""

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
        
        return d   

    def _test_chapters(self):
        """Example code to show use of Chapters"""

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
        
        return d           

        
    def _test_sections(self):
        """Example code to show use of Sections"""

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
        
        return d           

    def _test_tables(self):
        """Example code to show use of Tables"""

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
        
        return d                   

    def _test_figures(self):
        """Example code to show use of Figures"""

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
        
        return d  

    def _test_subfigures(self):
        """Example code to show use of SubFigures"""

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
                
        return d  

    def _test_pictures(self):
        """Example code to show use of a Picture environment"""

        d = Document(   classname='report',
                        options=['9pt', 'twoside'])    
        
        p = d.add(Picture(  width=80, 
                            height=70, 
                            unitlength='1mm', 
                            star=False,
                            placement='h',
                            caption='This is a drawing',
                            label='fig:Drawing'))                    

        p.add('\\def\\gridspace{20}\n')
        p.add('\\def\\doublegridspace{40}\n')
        p.add('\\def\\griddiagonal{10}\n')
        p.add('\\def\\griddot{\\circle*{2}}\n')
        p.add('\\linethickness{1.5pt}\n')

        # dots
        p.add(  '\\multiput(20, 10)(5, 5){3}'
                '{\\multiput(0, 0)(0, \\gridspace){3}'
                '{\\multiput(0, 0)(\\gridspace, 0){3}'
                '{\\griddot}}'
                '}\n')

        # straight lines
        p.add(  '\\multiput(20, 10)(5, 5){3}'
                '{\\multiput(0, 0)(0, \\gridspace){3}'
                '{\\line(1, 0){\\doublegridspace}}'
                '\\multiput(0, 0)(\\gridspace, 0){3}'
                '{\\line(0, 1){\\doublegridspace}}'
                '}\n')

        # diagonal lines
        p.add(  '\\multiput(20, 10)(0, \\gridspace){3}'
                '{\\multiput(0, 0)(\\gridspace, 0){3}'
                '{\\line(1, 1){\\griddiagonal}}'
                '}\n')

        p.add('\\linethickness{1pt}\n')

        # arrows
        p.add('\\put(20, 10){\\vector(-1, -1){5}}\n')
        p.add('\\put(30, 60){\\vector(0, 1){10}}\n')
        p.add('\\put(70, 20){\\vector(1, 0){10}}\n')

        # labels
        p.add('\\put(18, 12){\\makebox(0, 0){2}}\n')
        p.add('\\put(28, 62){\\makebox(0, 0){2}}\n')
        p.add('\\put(72, 22){\\makebox(0, 0){2}}\n')
        p.add('\\put(17, 4){\\makebox(0, 0){x}}\n')
        p.add('\\put(80, 18){\\makebox(0, 0){y}}\n')
        p.add('\\put(28, 70){\\makebox(0, 0){z}}\n')                    
                
        return d  

    def _test_multicolfigure(self):
        """Example code to show 2 figures in a multicol environment"""

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

        return d
        
    def _test_maketitle(self):
        """Example code to show 2 figures in a multicol environment"""

        d = Document(   classname='report',
                        options=['9pt', 'twoside'])    

        d.add(Command('title', ['Document Title']))
        d.add(Command('author', ['Author Name']))
        d.add(Command('date', ['2016-02-29']))
        d.add(Tag('maketitle'))
        
        return d        

if __name__ == '__main__':
    SelfTest().run()    
