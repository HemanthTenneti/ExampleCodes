# Create the DataFrame given below and export the content into tutor.csv file
from pandas import DataFrame
from numpy import NaN

tutorDetails = {
    "Tutor": ["Tahira", "Gurjyot", "Anusha", "Jacob", "Venkat"],
    "Classes": [28, NaN, 41, NaN, 40],
    "Country": ["USA", "UK", "Japan", "USA", "Brazil"],
}
tutorDF = DataFrame(tutorDetails)
print(tutorDF)
tutorDF.to_csv(r"Record Book Programs/Program Files/TutorData.csv")
