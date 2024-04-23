# Imported modules.

import csv
from datetime import datetime

# Call the now() method to get the current date and time as a datetime object from the computer's operating system.

current_date_and_time = datetime.now()

# Dictionary Key Index.

ID_INDEX = 0

# Dictionary info Index.

CALL_NUMBER_INDEX = 0
UNIT_ID_INDEX = 1
INCIDENT_NUMBER_INDEX = 2
CALL_TYPE_INDEX = 3
CALL_DATE_INDEX = 4
WATCH_DATE_INDEX = 5
RECEIVED_DTTM_INDEX = 6
ENTRY_DTTM_INDEX = 7
DISPATCH_DTTM_INDEX = 8
RESPONSE_DTTM_INDEX = 9
ON_SCENE_DTTM_INDEX = 10
TRANSPORT_DTTM_INDEX = 11
HOSPITAL_DTTM_INDEX = 12
CALL_FINAL_DISPOSITION_INDEX = 13
AVAILABLE_DTTM_INDEX = 14
ADDRESS_INDEX = 15
CITY_INDEX = 16
ZIP_CODE_OF_THE_INCIDENT_INDEX = 17
BATTALION_INDEX = 18
STATION_AREA_INDEX = 19
BOX_INDEX = 20
ORIGINAL_PRIORITY_INDEX = 21
PRIORITY_INDEX = 22
FINAL_PRIORITY_INDEX = 23
ALS_UNIT_INDEX = 24
CALL_TYPE_GROUP_INDEX = 25
NUMBER_OF_ALARMS_INDEX = 26
UNIT_TYPE_INDEX = 27
UNIT_SEQUENCE_IN_CALL_DISPATCH_INDEX = 28
FIRE_PREVENTION_DISTRICT_INDEX = 29
SUPERVISOR_DISTRICT_INDEX = 30
NEIGHBORHOODS_ANALYSIS_BOUNDARIES_INDEX = 31
ROW_ID_INDEX = 32
CASE_LOCATION_INDEX = 33
DATA_LOADED_AT_INDEX = 34
ANALYSIS_NEIGHBORHOODS_INDEX = 35

# functions

def main():
    """Main function of the program, it calls the other functions and prints the header of the program.y

    Parameters:
        None."""

    # First try block.
    try:

        # File path, please use the provided CSV file for the evaluation.
        regs_dict = file_reader("emergency_reg.csv",ID_INDEX)
        print(f"\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nEmergency Data Reader Build ALPHA 0.1\nSession timestamp: {current_date_and_time:%a %b %d %H:%M:%S %Y}\nTotal of entries registered: {len(regs_dict)}")

        # Loop that execute the function until the user select the break option.
        while True:
            
            # Second try block.
            try:

                user_selection = int(input("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------\n\n1: Search a specific entry.\n2: Save a specific entry into a txt file.\n3: Get all the entries.\n4: Save all the entries into a txt file.\n0: Exit the program.\nSelection: "))

                if user_selection == 1:
                    get_specific_info(regs_dict, user_selection)

                elif user_selection == 2:
                    get_specific_info(regs_dict, user_selection)

                elif user_selection == 3:
                    get_general_info(regs_dict)

                elif user_selection == 4:
                    print_general_info(regs_dict)

                elif user_selection == 0:
                    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nGoodbye\n")
                    break

                # invalid int handler.
                else:
                    print(f"\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nSelect a valid option.")

            # Value error handler.
            except ValueError:
                print(f"\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nSelect a valid option.")

    # File error handler.
    except FileNotFoundError as not_file_found_err:
        # This code will be executed if the csv files are not found.
        print(f"\n", type(not_file_found_err).__name__, not_file_found_err, sep=": ")

def file_reader(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file."""
    
    regs_dict = {}

    # Open a file named dentists.csv and store a reference to the opened file in a variable named reg_csv_file.
    with open(filename, "rt") as reg_csv_file:

        # Use the csv module to create a reader object that will read from the opened file.
        reader = csv.reader(reg_csv_file)

        # The first row of the CSV file contains column headings and not data of the emergency database; this statement skips the first row of the CSV file.
        next(reader)

        # Read each row in the CSV file one at a time. The reader object returns each row as a list.
        for info in reader:
            if len(info) != 0:
                key = info[key_column_index]
                regs_dict[key] = info
    
    # Retuns the Dictionary.
    return regs_dict

def get_specific_info(regs_dict, user_selection):
    """Function that ask for a specific registered entry key to the user.

    Parameters:
        regs_dict: The dictionary that contains all the info."""
    
    # loop for the Call Number.
    while True:

        # Try block.
        try:
            key = int(input(f"\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nInsert The nine digit Call Number (Example 233092121): "))
            # Key length filter.
            if len(str(key)) > 9:
                print(f"\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nMore than nine digits detected. Insert a valid code.")
            elif len(str(key)) < 9:
                print(f"\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nLess than nine digits detected. Insert a valid code.")
            else:
                if user_selection == 1:
                    retrieve_specific_info(regs_dict, key)
                elif user_selection == 2:
                    print_specific_info(regs_dict, key)
                break
        
        # Error handler.
        except ValueError:
            print(f"\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nInsert a valid Call Number.")

def retrieve_specific_info(regs_dict, key):
    """Function that ask for a specific registered entry key to the user.

    Parameters:
        regs_dict: The dictionary that contains all the info.
        key: the key of the entry."""
    print("\n" + "-" * 150)
    key_str = str(key)
    if key_str not in regs_dict:
        print(f"\n Register not found")
    else:
        # If statement that search and separate the entry data.
        if key_str in regs_dict:
            data = regs_dict[key_str]
            unit_id = data[UNIT_ID_INDEX]
            incident_number = data[INCIDENT_NUMBER_INDEX]
            call_type = data[CALL_TYPE_INDEX]
            call_date = data[CALL_DATE_INDEX]
            watch_date = data[WATCH_DATE_INDEX]
            received_dttm = data[RECEIVED_DTTM_INDEX]
            entry_dttm = data[ENTRY_DTTM_INDEX]
            dispatch_dttm = data[DISPATCH_DTTM_INDEX]
            response_dttm = data[RESPONSE_DTTM_INDEX]
            on_scene_dttm = data[ON_SCENE_DTTM_INDEX]
            transport_dttm = data[TRANSPORT_DTTM_INDEX]
            hospital_dttm = data[HOSPITAL_DTTM_INDEX]
            call_final_disposition = data[CALL_FINAL_DISPOSITION_INDEX]
            available_dttm = data[AVAILABLE_DTTM_INDEX]
            address = data[ADDRESS_INDEX]
            city = data[CITY_INDEX]
            zip_code_of_the_incident = data[ZIP_CODE_OF_THE_INCIDENT_INDEX]
            battalion = data[BATTALION_INDEX]
            station_area = data[STATION_AREA_INDEX]
            box = data[BOX_INDEX]
            original_priority = data[ORIGINAL_PRIORITY_INDEX]
            priority = data[PRIORITY_INDEX]
            final_priority = data[FINAL_PRIORITY_INDEX]
            als_unit = data[ALS_UNIT_INDEX]
            call_type_group = data[CALL_TYPE_GROUP_INDEX]
            number_of_alarms = data[NUMBER_OF_ALARMS_INDEX]
            unit_type = data[UNIT_TYPE_INDEX]
            unit_sequence_in_call_dispatch = data[UNIT_SEQUENCE_IN_CALL_DISPATCH_INDEX]
            fire_prevention_district = data[FIRE_PREVENTION_DISTRICT_INDEX]
            supervisor_district = data[SUPERVISOR_DISTRICT_INDEX]
            neighborhoods_analysis_boundaries = data[NEIGHBORHOODS_ANALYSIS_BOUNDARIES_INDEX]
            row_id = data[ROW_ID_INDEX]
            case_location = data[CASE_LOCATION_INDEX]
            data_loaded_at = data[DATA_LOADED_AT_INDEX]
            analysis_neighborhoods = data[ANALYSIS_NEIGHBORHOODS_INDEX]

        # Print the results for the user to see.
        print(f"\nCall Number: {key}\nUnit ID: {unit_id}\nIncident Number: {incident_number}\nCall Type: {call_type}\nCall Date: {call_date}\nWatch Date: {watch_date}\nReceived Date Time: {received_dttm}\nEntry Date Time: {entry_dttm}\nDispatch Date Time: {dispatch_dttm}\nResponse Date Time: {response_dttm}\nOn Scene Date Time: {on_scene_dttm}\nTransport Date Time: {transport_dttm}\nHospital Date Time: {hospital_dttm}\nCall Final Disposition: {call_final_disposition}\nAvailable Date Time: {available_dttm}\nAdress: {address}\nCity: {city}\nZip Code of the Incident: {zip_code_of_the_incident}\nBattalion: {battalion}\nStation Area: {station_area}\nBox: {box}\nOriginal Priority: {original_priority}\nPriority: {priority}\nFinal Priority: {final_priority}\nALS Unit: {als_unit}\nCall Type Group: {call_type_group}\nNumber of Alarms: {number_of_alarms}\nUnit Type: {unit_type}\nUnit Sequence in Call Dispatch: {unit_sequence_in_call_dispatch}\nFire Prevention District: {fire_prevention_district}\nSupervisor District: {supervisor_district}\nNeighborhoods Analysis Boundaries: {neighborhoods_analysis_boundaries}\nRow ID: {row_id}\nCase Location: {case_location}\nData Loaded at: {data_loaded_at}\nAnalysis Neighborhoods: {analysis_neighborhoods}")

def print_specific_info(regs_dict, key):
    """Function that write in a TXT file the specific registered entry required by the user.

    Parameters:
        regs_dict: The dictionary that contains all the info.
        key: the key of the entry."""
    print("\n" + "-" * 150)
    key_str = str(key)
    if key_str not in regs_dict:
        print(f"\n Register not found")
    else:
        # Open the text file for writing and store a reference to the opened file in a variable named text_file that will be separated into other variables.
        with open("individual_report.txt", "wt") as text_file:

            # If statement that search and separate the entry data.
            if key_str in regs_dict:
                data = regs_dict[key_str]
                unit_id = data[UNIT_ID_INDEX]
                incident_number = data[INCIDENT_NUMBER_INDEX]
                call_type = data[CALL_TYPE_INDEX]
                call_date = data[CALL_DATE_INDEX]
                watch_date = data[WATCH_DATE_INDEX]
                received_dttm = data[RECEIVED_DTTM_INDEX]
                entry_dttm = data[ENTRY_DTTM_INDEX]
                dispatch_dttm = data[DISPATCH_DTTM_INDEX]
                response_dttm = data[RESPONSE_DTTM_INDEX]
                on_scene_dttm = data[ON_SCENE_DTTM_INDEX]
                transport_dttm = data[TRANSPORT_DTTM_INDEX]
                hospital_dttm = data[HOSPITAL_DTTM_INDEX]
                call_final_disposition = data[CALL_FINAL_DISPOSITION_INDEX]
                available_dttm = data[AVAILABLE_DTTM_INDEX]
                address = data[ADDRESS_INDEX]
                city = data[CITY_INDEX]
                zip_code_of_the_incident = data[ZIP_CODE_OF_THE_INCIDENT_INDEX]
                battalion = data[BATTALION_INDEX]
                station_area = data[STATION_AREA_INDEX]
                box = data[BOX_INDEX]
                original_priority = data[ORIGINAL_PRIORITY_INDEX]
                priority = data[PRIORITY_INDEX]
                final_priority = data[FINAL_PRIORITY_INDEX]
                als_unit = data[ALS_UNIT_INDEX]
                call_type_group = data[CALL_TYPE_GROUP_INDEX]
                number_of_alarms = data[NUMBER_OF_ALARMS_INDEX]
                unit_type = data[UNIT_TYPE_INDEX]
                unit_sequence_in_call_dispatch = data[UNIT_SEQUENCE_IN_CALL_DISPATCH_INDEX]
                fire_prevention_district = data[FIRE_PREVENTION_DISTRICT_INDEX]
                supervisor_district = data[SUPERVISOR_DISTRICT_INDEX]
                neighborhoods_analysis_boundaries = data[NEIGHBORHOODS_ANALYSIS_BOUNDARIES_INDEX]
                row_id = data[ROW_ID_INDEX]
                case_location = data[CASE_LOCATION_INDEX]
                data_loaded_at = data[DATA_LOADED_AT_INDEX]
                analysis_neighborhoods = data[ANALYSIS_NEIGHBORHOODS_INDEX]

            # Print the results for the user to see.
            print(f"\nCall Number: {key}\nUnit ID: {unit_id}\nIncident Number: {incident_number}\nCall Type: {call_type}\nCall Date: {call_date}\nWatch Date: {watch_date}\nReceived Date Time: {received_dttm}\nEntry Date Time: {entry_dttm}\nDispatch Date Time: {dispatch_dttm}\nResponse Date Time: {response_dttm}\nOn Scene Date Time: {on_scene_dttm}\nTransport Date Time: {transport_dttm}\nHospital Date Time: {hospital_dttm}\nCall Final Disposition: {call_final_disposition}\nAvailable Date Time: {available_dttm}\nAdress: {address}\nCity: {city}\nZip Code of the Incident: {zip_code_of_the_incident}\nBattalion: {battalion}\nStation Area: {station_area}\nBox: {box}\nOriginal Priority: {original_priority}\nPriority: {priority}\nFinal Priority: {final_priority}\nALS Unit: {als_unit}\nCall Type Group: {call_type_group}\nNumber of Alarms: {number_of_alarms}\nUnit Type: {unit_type}\nUnit Sequence in Call Dispatch: {unit_sequence_in_call_dispatch}\nFire Prevention District: {fire_prevention_district}\nSupervisor District: {supervisor_district}\nNeighborhoods Analysis Boundaries: {neighborhoods_analysis_boundaries}\nRow ID: {row_id}\nCase Location: {case_location}\nData Loaded at: {data_loaded_at}\nAnalysis Neighborhoods: {analysis_neighborhoods}", file=text_file)

        # Print a completation message.
        print(f"\nTask Completed.")


def get_general_info(regs_dict):
    """Function that prints all the registered entries in the dictionary.

    Parameters:
        regs_dict: The dictionary that contains all the info."""
    print("\n" + "-" * 150)

    # for loop that separate the entry data.
    for key in regs_dict:
        data = regs_dict[key]
        unit_id = data[UNIT_ID_INDEX]
        incident_number = data[INCIDENT_NUMBER_INDEX]
        call_type = data[CALL_TYPE_INDEX]
        call_date = data[CALL_DATE_INDEX]
        watch_date = data[WATCH_DATE_INDEX]
        received_dttm = data[RECEIVED_DTTM_INDEX]
        entry_dttm = data[ENTRY_DTTM_INDEX]
        dispatch_dttm = data[DISPATCH_DTTM_INDEX]
        response_dttm = data[RESPONSE_DTTM_INDEX]
        on_scene_dttm = data[ON_SCENE_DTTM_INDEX]
        transport_dttm = data[TRANSPORT_DTTM_INDEX]
        hospital_dttm = data[HOSPITAL_DTTM_INDEX]
        call_final_disposition = data[CALL_FINAL_DISPOSITION_INDEX]
        available_dttm = data[AVAILABLE_DTTM_INDEX]
        address = data[ADDRESS_INDEX]
        city = data[CITY_INDEX]
        zip_code_of_the_incident = data[ZIP_CODE_OF_THE_INCIDENT_INDEX]
        battalion = data[BATTALION_INDEX]
        station_area = data[STATION_AREA_INDEX]
        box = data[BOX_INDEX]
        original_priority = data[ORIGINAL_PRIORITY_INDEX]
        priority = data[PRIORITY_INDEX]
        final_priority = data[FINAL_PRIORITY_INDEX]
        als_unit = data[ALS_UNIT_INDEX]
        call_type_group = data[CALL_TYPE_GROUP_INDEX]
        number_of_alarms = data[NUMBER_OF_ALARMS_INDEX]
        unit_type = data[UNIT_TYPE_INDEX]
        unit_sequence_in_call_dispatch = data[UNIT_SEQUENCE_IN_CALL_DISPATCH_INDEX]
        fire_prevention_district = data[FIRE_PREVENTION_DISTRICT_INDEX]
        supervisor_district = data[SUPERVISOR_DISTRICT_INDEX]
        neighborhoods_analysis_boundaries = data[NEIGHBORHOODS_ANALYSIS_BOUNDARIES_INDEX]
        row_id = data[ROW_ID_INDEX]
        case_location = data[CASE_LOCATION_INDEX]
        data_loaded_at = data[DATA_LOADED_AT_INDEX]
        analysis_neighborhoods = data[ANALYSIS_NEIGHBORHOODS_INDEX]

        # Print the results for the user to see.
        print(f"\nCall Number: {key}\nUnit ID: {unit_id}\nIncident Number: {incident_number}\nCall Type: {call_type}\nCall Date: {call_date}\nWatch Date: {watch_date}\nReceived Date Time: {received_dttm}\nEntry Date Time: {entry_dttm}\nDispatch Date Time: {dispatch_dttm}\nResponse Date Time: {response_dttm}\nOn Scene Date Time: {on_scene_dttm}\nTransport Date Time: {transport_dttm}\nHospital Date Time: {hospital_dttm}\nCall Final Disposition: {call_final_disposition}\nAvailable Date Time: {available_dttm}\nAdress: {address}\nCity: {city}\nZip Code of the Incident: {zip_code_of_the_incident}\nBattalion: {battalion}\nStation Area: {station_area}\nBox: {box}\nOriginal Priority: {original_priority}\nPriority: {priority}\nFinal Priority: {final_priority}\nALS Unit: {als_unit}\nCall Type Group: {call_type_group}\nNumber of Alarms: {number_of_alarms}\nUnit Type: {unit_type}\nUnit Sequence in Call Dispatch: {unit_sequence_in_call_dispatch}\nFire Prevention District: {fire_prevention_district}\nSupervisor District: {supervisor_district}\nNeighborhoods Analysis Boundaries: {neighborhoods_analysis_boundaries}\nRow ID: {row_id}\nCase Location: {case_location}\nData Loaded at: {data_loaded_at}\nAnalysis Neighborhoods: {analysis_neighborhoods}")

def print_general_info(regs_dict):
    """Function that saves into a TXT file all the registered entries in the dictionary.

    Parameters:
        regs_dict: The dictionary that contains all the info."""
    print("\n" + "-" * 150)

    # Open the text file for writing and store a reference to the opened file in a variable named text_file that will be separated into other variables.
    with open("general_report.txt", "wt") as text_file:

        # for loop that separate the entry data.
        for key in regs_dict:
            data = regs_dict[key]
            unit_id = data[UNIT_ID_INDEX]
            incident_number = data[INCIDENT_NUMBER_INDEX]
            call_type = data[CALL_TYPE_INDEX]
            call_date = data[CALL_DATE_INDEX]
            watch_date = data[WATCH_DATE_INDEX]
            received_dttm = data[RECEIVED_DTTM_INDEX]
            entry_dttm = data[ENTRY_DTTM_INDEX]
            dispatch_dttm = data[DISPATCH_DTTM_INDEX]
            response_dttm = data[RESPONSE_DTTM_INDEX]
            on_scene_dttm = data[ON_SCENE_DTTM_INDEX]
            transport_dttm = data[TRANSPORT_DTTM_INDEX]
            hospital_dttm = data[HOSPITAL_DTTM_INDEX]
            call_final_disposition = data[CALL_FINAL_DISPOSITION_INDEX]
            available_dttm = data[AVAILABLE_DTTM_INDEX]
            address = data[ADDRESS_INDEX]
            city = data[CITY_INDEX]
            zip_code_of_the_incident = data[ZIP_CODE_OF_THE_INCIDENT_INDEX]
            battalion = data[BATTALION_INDEX]
            station_area = data[STATION_AREA_INDEX]
            box = data[BOX_INDEX]
            original_priority = data[ORIGINAL_PRIORITY_INDEX]
            priority = data[PRIORITY_INDEX]
            final_priority = data[FINAL_PRIORITY_INDEX]
            als_unit = data[ALS_UNIT_INDEX]
            call_type_group = data[CALL_TYPE_GROUP_INDEX]
            number_of_alarms = data[NUMBER_OF_ALARMS_INDEX]
            unit_type = data[UNIT_TYPE_INDEX]
            unit_sequence_in_call_dispatch = data[UNIT_SEQUENCE_IN_CALL_DISPATCH_INDEX]
            fire_prevention_district = data[FIRE_PREVENTION_DISTRICT_INDEX]
            supervisor_district = data[SUPERVISOR_DISTRICT_INDEX]
            neighborhoods_analysis_boundaries = data[NEIGHBORHOODS_ANALYSIS_BOUNDARIES_INDEX]
            row_id = data[ROW_ID_INDEX]
            case_location = data[CASE_LOCATION_INDEX]
            data_loaded_at = data[DATA_LOADED_AT_INDEX]
            analysis_neighborhoods = data[ANALYSIS_NEIGHBORHOODS_INDEX]

            # Save the results into the TXT file.
            print(f"\nCall Number: {key}\nUnit ID: {unit_id}\nIncident Number: {incident_number}\nCall Type: {call_type}\nCall Date: {call_date}\nWatch Date: {watch_date}\nReceived Date Time: {received_dttm}\nEntry Date Time: {entry_dttm}\nDispatch Date Time: {dispatch_dttm}\nResponse Date Time: {response_dttm}\nOn Scene Date Time: {on_scene_dttm}\nTransport Date Time: {transport_dttm}\nHospital Date Time: {hospital_dttm}\nCall Final Disposition: {call_final_disposition}\nAvailable Date Time: {available_dttm}\nAdress: {address}\nCity: {city}\nZip Code of the Incident: {zip_code_of_the_incident}\nBattalion: {battalion}\nStation Area: {station_area}\nBox: {box}\nOriginal Priority: {original_priority}\nPriority: {priority}\nFinal Priority: {final_priority}\nALS Unit: {als_unit}\nCall Type Group: {call_type_group}\nNumber of Alarms: {number_of_alarms}\nUnit Type: {unit_type}\nUnit Sequence in Call Dispatch: {unit_sequence_in_call_dispatch}\nFire Prevention District: {fire_prevention_district}\nSupervisor District: {supervisor_district}\nNeighborhoods Analysis Boundaries: {neighborhoods_analysis_boundaries}\nRow ID: {row_id}\nCase Location: {case_location}\nData Loaded at: {data_loaded_at}\nAnalysis Neighborhoods: {analysis_neighborhoods}", file=text_file)

    # Print a completation message.
    print(f"\nTask Completed.")

# Call main to start this program.
if __name__ == "__main__":
    main()