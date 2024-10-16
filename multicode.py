import os, sys
import arcpy
 
def worker(clipper, tobeclipped, field, oid, outputFolder):
    """  
       This is the function that gets called and does the work of clipping the input feature class to one of the polygons from the clipper feature class. 
       Note that this function does not try to write to arcpy.AddMessage() as nothing is ever displayed.  If the clip succeeds then it returns TRUE else FALSE.  
    """
    try:   
        # Create a layer with only the polygon with ID oid. Each clipper layer needs a unique name, so we include oid in the layer name.
        query = '"' + field +'" = ' + str(oid)
        arcpy.AddMessage("Printing query: " + query)
        arcpy.MakeFeatureLayer_management(clipper, "clipper_" + str(oid), query) 
        
        # Do the clip. We include the oid in the name of the output feature class. 
        outFC = outputFolder + str(oid) + ".shp"
        arcpy.Clip_analysis(tobeclipped, "clipper_" + str(oid), outFC) 
         
        print("finished clipping:", str(oid)) 
        return True # everything went well so we return True
    except Exception as e:
        # Some error occurred so return False
        arcpy.AddError(str(e))
        print("Exception:", e)
        return False