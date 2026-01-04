from unstructured.partition.pdf import partition_pdf

# unstructured package is supported for OCR, texts, tables extraction
def ExtractTextFromPDF(filePath):
    ele = partition_pdf(filePath)
    return " ".join([str(e) for e in ele])
    