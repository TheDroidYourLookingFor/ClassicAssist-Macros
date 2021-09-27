import clr
import System
from Assistant import Engine
from ClassicAssist.UO.Data import Layer

clr.AddReference("System.Core")
clr.ImportExtensions(System.Linq)

def GetBackpackWeight(serial):
    mobile = Engine.Mobiles.GetMobile(serial)
    
    if mobile == None:
        print 'Mobile not found'
        return -1
    
    layerSerial = mobile.GetLayer(Layer.Backpack)

    if layerSerial == 0:
        return -1
        
    layerItem = Engine.Items.GetItem(layerSerial)
    if WaitForProperties(layerItem, 5000):
        prop = layerItem.Properties.FirstOrDefault(lambda i: i.Cliloc == 1050044)

        if prop:
            return prop.Arguments[1]
        else:
            return -1        
    else:
        return -1
        
print GetBackpackWeight(0xf642)