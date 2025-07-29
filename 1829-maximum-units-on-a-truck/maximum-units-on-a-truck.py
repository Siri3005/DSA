class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        count=0
        units=0
        for box in boxTypes:
            if count==truckSize:
                return units
            else:
                if box[0]+count<truckSize:
                    count+=box[0]
                    units+=box[0]*box[1]
                else:
                    left=truckSize-count
                    count+=left
                    units+=left*box[1]
        return units
            

