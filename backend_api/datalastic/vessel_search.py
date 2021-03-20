# -*- coding: utf-8 -*-
from . import main


class Vessel_search(main.Datalastic):

    def __init__(self, api_key) -> None:
        super().__init__(api_key)
        self.endpoint = "/api/v0/vessel_find"

    def get_port_by_name(self,name=None,fuzzy=None , port_type=None, country_iso=None, gross_tonnage_min=None, gross_tonnage_max=None, deadweight_min=None , deadweight_max=None , length_min=None, length_max=None, breadth_min=None, breadth_max=None, year_build_min=None , year_build_max=None):
        parameters = {"api-key":self.api_key, "name": name}
        if name:
            parameters.update({"name":name})
        if fuzzy:
            parameters.update({"fuzzy":fuzzy})
        if port_type:
            parameters.update({"type":port_type})
        if country_iso:
            parameters.update({"country_iso":country_iso})
        if gross_tonnage_min:
            parameters.update({"gross_tonnage_min":gross_tonnage_min})
        if gross_tonnage_max:
            parameters.update({" gross_tonnage_max": gross_tonnage_max})
        if deadweight_min:
            parameters.update({"deadweight_min":deadweight_min})
        if deadweight_max:
            parameters.update({"deadweight_max":deadweight_max})
        if length_min:
            parameters.update({"length_min":length_min})
        if length_max:
            parameters.update({"length_max":length_max})
        if breadth_min:
            parameters.update({"breadth_min":breadth_min})
        if breadth_max:
            parameters.update({"breadth_max":breadth_max})
        if year_build_min:
            parameters.update({"year_build_min":year_build_min})
        if year_build_max:
            parameters.update({"year_build_max":year_build_max})
         
        return self._get_results(url=f"{self.url}{self.endpoint}", parameters=parameters)

       
if __name__ == "__main__":
    api = Vessel_search()