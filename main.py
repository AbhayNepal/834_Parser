import pyx12
from pyx12.x12context import X12ContextReader
import pyx12.error_handler as error_handler
from pyx12.params import ParamsUnix


file_content = X12ContextReader(ParamsUnix(),error_handler,"834_ls_le_ls.txt")
vendorDetails = []

for isaDataLoop in file_content.iter_segments("ISALOOP"):
    if(isaDataLoop.get_value('ISA05')):
        vendorDetails.append(isaDataLoop.get_value('ISA05'))

print(vendorDetails)


