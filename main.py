budget = 0
import xlrd
import matplotlib.pyplot as plt
import numpy as np
from typing import (
    Generic,
    TypeVar
)

from base import BaseFarm

'''def _check_validcrop(crop):
    if (crop not in {'barley': '1', 'corn': '2', 'cotton': '3', 'wheat': '4', 'rice': '5', 'sorghum': '6', 'soybean': '7'}):
        raise ValueError(f"Invalid crop, chose {crop}, which it not in the list. Please choose one of the following: barley, corn, cotton, wheat, rice, sorgum, or soybean")'''
    
def crop_ID(crop):
    
    crop_list = {'barley': '1', 'corn': '2', 'cotton': '3', 'wheat': '4', 'rice': '5', 'sorghum': '6', 'soybean': '7'}
    
    return crop_list[crop]
    
GenericFarm = TypeVar("GenericFarm", bound=BaseFarm)

class FarmAnalysis(Generic[GenericFarm]):  
    
    location2 = "C:\\Users\\Quinn\\Desktop\\Derived_CostofLiving_Data.xls"
    wb2 = xlrd.open_workbook(location2)
    sheet2 = wb2.sheet_by_index(0)      
    
    def __init__(
        self,
        crop='corn',
        equipment=[460000,480000,300000,130000,90000,30000],
        cost_per_liter1 = 1.33,
        cost_per_liter2 = 1.318,
        acres=10,
        bushels=0,
        country='United States',
        need_herbicide = True,
        need_fertilizer = True
    ):    
        cropID = crop_ID(crop)
        self.clear()
    
    def clear(self):
        
        self.data_list = []
        self.data_cache = None
    
    def seed_cost(acres, bushels, crop_specified):
        
        acre_cost = {'1': 20.94,'2': 95.06,'3': 85.84,'4': 14.86,'5': 92.29,'6': 14.13,'7': 63.37}
        
        bushels_per_acre = {'1': 60.4,'2': 177,'3': 19.29,'4': 44.3,'5': 126.9,'6': 69,'7': 51.4}
        
        acres = acres - (bushels / bushels_per_acre[crop_specified])
        
        return float(int(acre_cost[crop_specified] * acres * 100))/100
        
    def equipment_cost(tractor = True, sprayer = True, harvester = True, manure_spreader = True, cultivator = True, seeder = True, *args):
        
        return ([*args][0] * (tractor == True)) + ([*args][1] * (sprayer == True)) + ([*args][2] * (harvester == True)) + ([*args][3] * (manure_spreader == True)) + ([*args][4] * (cultivator == True)) + ([*args][5] * (seeder == True))
    
    def fuel(acres, cost_per_liter1 = 1.09):
        return float(int(acres/3 * 4.8 * 3.79 * cost_per_liter1 * 100))/100
    
    def fertilizer(acres, cost_per_liter2 = .52):
        return float(int(acres/8*cost_per_liter2*1000 * 100))/100
    
    def herbicide(acres, cost_per_liter3 = 10.04):
        return float(int(acre * 40 * cost_per_liter3 * 100))/100
    
    def rent_index(sheet):
        
        data_set = dict()
        for i in range(1,sheet.nrows):
            data_set[sheet.cell_value(i,0)] = [sheet.cell_value(i,2)]
            
        return data_set    
            
    def land_rent(acres, country, data_set):
        index = data_set[country]
        return float(int(acres * per_acre * index/46.86 * 12) * 100)/100
            
    def overall_cost(*args):
    
        return sum({*args,})
        
    def pie_chart(seed_cost = 0, equipment_cost = 0, fuel_cost = 0, fertilizer_cost = 0, rent_cost = 0, herbicide_cost = 0):
        
        mylabels = []
        label_array = {'Seeds': seed_cost, 'Equipment': equipment_cost, 'Fuel': fuel_cost, 'Fertilizer': fertilizer_cost, 'Rent': rent_cost, 'Herbicide': herbicide_cost}
        for element in label_array:
            if label_array[element] > max([seed_cost, equipment_cost, fuel_cost, fertilizer_cost, rent_cost, herbicide_cost])/100:
                mylabels.append(element)
                
        return plt.pie(np.array([i for i in [seed_cost, equipment_cost, fuel_cost, fertilizer_cost, rent_cost, herbicide_cost] if i > max([seed_cost, equipment_cost, fuel_cost, fertilizer_cost, rent_cost, herbicide_cost])/100]), labels = mylabels)
    
    def makeFarm(self, **kwargs):
        cost_array = []
        if need_fertilizer:
            cost_array.append(fertilizer(acres, cost_per_liter2))
        else:
            cost_array.append(0)
        if need_herbicide:
            cost_array.append(herbicide(acres, cost_per_liter3))
        else:
            cost_array.append(0)        
        cost_array.append(seed_cost(acres, bushels, cropID))
        cost_array.append(fuel(acres, cost_per_liter1))
        cost_array.append(equipment_cost(equipment, **kwargs))        
        cost_array.append(land_rent(acres, country, rent_index(sheet2)))
        cost_array.append(overall_cost(cost_array))