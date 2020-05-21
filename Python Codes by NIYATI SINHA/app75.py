from app72_find_max import find_max
list=[10,3,6,2]
maximum=find_max(list)
print(f"inbuit function max():{max(list)}")                #shadows means that there is already a predefined function max()
print(f"user defined function find_max(): {maximum}")          # which returns the max value
                                                    #thus it means we are overwritting the inbuilt function meaning
                                                    #which is considered as a bad programming practice
                                                    #as we have overriten the meaning of max it cannot be used to call the inbuit function