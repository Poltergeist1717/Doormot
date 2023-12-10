from .models import To_Let_Listed_Properties, For_Sale_Listed_Properties
from doormot_app.doormot_app_modules import return_user_object
import logging

logger = logging.getLogger(__name__)




# Type: Class
# Name: Post Property View
# Methods: __init__, load_property_models_in_batches, get_filtered_queryset 
# Tasks: Handles uploading property
#        Handles upload logic for property types
#        Prevents users not allowed to upload property
#        Reverse changes made to database if any of the transactions fails (@transaction.atomic) 
#        Handles creating property instnance for both types - For Sale and To Let
#        Handles creating property image instance for both types - For Sale and To Let


class load_property_objects:

    def __init__(self, model):
        self.model = model

    def load_property_models_in_batches(self, desired_no_of_proprties_to_load):
            
        property_model_objects = self.model.objects.all()

        list_of_properties_in_batches = []

        listed_properties_length = len(property_model_objects)

        length_of_current_batch = len(list_of_properties_in_batches)

        desired_no_of_proprties_to_load = None
        counter = 0       
        if desired_no_of_proprties_to_load is not None:
            load_this_no_of_properties = desired_no_of_proprties_to_load
        else:
            load_this_no_of_properties = 39


        for property_object in property_model_objects:
            try:
                if listed_properties_length != 0:
                    current_property = property_model_objects[counter]
                    list_of_properties_in_batches.append(current_property)
                    counter += 1

                    if counter == load_this_no_of_properties:
                        counter = load_this_no_of_properties

                        if desired_no_of_proprties_to_load:
                            load_this_no_of_properties += desired_no_of_proprties_to_load
                        else:
                            load_this_no_of_properties += 39 

                        yield list_of_properties_in_batches
                        list_of_properties_in_batches = []

                    elif (length_of_current_batch < 40 or length_of_current_batch < desired_no_of_proprties_to_load) and counter == listed_properties_length:
                        load_this_no_of_properties = 39
                        counter = 0
                        desired_no_of_proprties_to_load = None 

                        yield list_of_properties_in_batches
                        list_of_properties_in_batches = []
                else:
                    return None
            except Exception as e:
                logger.exception("There was an error: %s", e)
                raise Exception(f"An error occurred: {e}")

    @staticmethod
    def get_filtered_queryset(model, filter_conditions=None):

        print(f"Model inside the module: {model}")
        print(f"First print: Filter conditions inside the module: {filter_conditions}")

        queryset = model.objects.all()

        if filter_conditions:
            print(f"Second Print: Filter conditions inside the module: {filter_conditions}")
            queryset = queryset.filter(**filter_conditions)
            print(f"First Queryset inside the module: {queryset}")

            if queryset.exists():
                print(f"Second Queryset inside the module if exist: {queryset}")
                return queryset
        else:
            return None