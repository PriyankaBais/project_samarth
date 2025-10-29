import pandas as pd

from data_handler import get_agriculture_data, get_climate_data

def answer_question(question):
    """
    Parses a question and returns a formatted answer and sources.
    This is the "brain" of your prototype.
    """
    
    question_lower = question.lower()
    
    
    if "rainfall" in question_lower and ("production" in question_lower or "crop" in question_lower):
        
        try:
            
            agri_df, agri_source = get_agriculture_data()
            climate_df, climate_source = get_climate_data()

            
            combined_df = pd.merge(
                agri_df, 
                climate_df, 
                on=["State", "Year"], 
                how="inner"
            )

           
            target_state = 'Uttar Pradesh'
            target_crop = 'Rice'
            
            filtered_data = combined_df[
                (combined_df['State'] == target_state) &
                (combined_df['Crop_Type'] == target_crop)
            ]

            
            if filtered_data.empty:
                answer_string = f"I found data, but there was no matching information for '{target_crop}' in '{target_state}'."
            else:
                answer_string = f"Here is the comparison for {target_crop} production and rainfall in {target_STATE}:\n\n"
               
                for index, row in filtered_data.iterrows():
                    answer_string += (
                        f"  - **Year: {row['Year']}**\n"
                        f"    Rainfall: {row['Rainfall']} mm\n"
                        f"    Production: {row['Production']} Tonnes\n\n"
                    )

        
            sources = [
                f"Agriculture Data: {agri_source}",
                f"Climate Data: {climate_source}"
            ]
            
            return answer_string, sources
        
        except Exception as e:
          
            return f"An error occurred while processing your request: {e}", []

    else:
    
        return (
            "Sorry, this prototype can only answer questions that compare "
            "crop production and rainfall. \n\n"
            "Try asking: 'Compare rainfall and crop production.'"
        ), []