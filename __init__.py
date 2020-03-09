# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:33:08 2020

@author: Dineshkumar M
"""

import PyPDF2


def pdf_classify(file):
    if file.endswith('.pdf') or file.endswith('.PDF'):
        opened_pdf = PyPDF2.PdfFileReader(file, 'rb')
        if opened_pdf.isEncrypted:
            opened_pdf.decrypt("")

        p = opened_pdf.getPage(0)
        p_text = p.extractText()

        if len(p_text) > 40:
            print(file, 'is digital pdf')
            return 1
        else:
            if (len(p_text)) > 0:
                if 'scanned' or 'scan' in p_text.lower():
                    print(file, 'is scanned pdf')
                    print(p_text)
                    return 0
                else:
                    return 1
            else:
                print(file, 'is scanned pdf')
                return 0
    else:
        print(file, 'not a pdf file')
        return 0
