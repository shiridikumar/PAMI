import random as _rd
import sys as _sys


class createSyntheticGeoreferentialTemporal:
    """
        This class create synthetic geo-referential temporal database. 

        Attribute:
        ----------
        transactions : pandas.DataFrame
            No of transactions
        items : int or float
            No of items
        avgTransaction : str
            The length of average transaction
        outputFile: str
            Name of the output file.

        Methods:
        --------
        getGeoreferentialTemporalDatabase(outputFile)
            Create geo-referential temporal database store into outputFile

        Credits:
        ---------
             The complete program was written by  P.Likhitha   under the supervision of Professor Rage Uday Kiran.

    """
    
    def __init__(self, transactions, items, avgTransaction):
        self._transactions = transactions
        self._items = items
        self._avgTransaction = avgTransaction
    
    def createGeoreferentialTemporalDatabase(self, outputFile):
        """
        create transactional database and return outputFileName
        :param outputFile: file name or path to store database
        :type outputFile: str
        :return: outputFile name
        """
        writer = open(outputFile, 'w+')
        items = []
        count = 1
        for i in range(self._items):
            lat = _rd.randint(1, self._items)
            lon = _rd.randint(1, self._items)
            if lat == lon:
                lon = _rd.randint(1, self._items)
            stt = '(' + str(lat) + ' ' + str(lon) + ')'
            items.append(stt)
        for i in range(self._transactions):
            length = _rd.randint(1, self._avgTransaction + 20)
            st = str(count)
            for i in range(length):
                rd = _rd.randint(0, len(items) - 1)
                item = items[rd]
                st = st + str(item) + '\t'
            writer.write("%s \n" % st)
            count += 1
            
if __name__ == "__main__":
    _ap = str()
    _ap = createSyntheticGeoreferentialTemporal(100000, 870, 10)
    _ap.createGeoreferentialTemporalDatabase("T10_geo_temp.txt")
else:
    print("Error! The number of input parameters do not match the total number of parameters provided")