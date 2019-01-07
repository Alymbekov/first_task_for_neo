import json
file_name = "personalinformation.json"
my_file = open("personalinformation.json",mode="w")
personal_information_of_me = {
    
    "first_name":"Dastan",
    "last_name":"Alymbekov",
    
    "details_of_me":{
       
        "age":21,
        "height":169,
        "weight":55,
        "national":"KYRGYZ"
    },
    "language":{
       
        "first_language":"Kyrgyz",
        "second_language":"Russia",
        "third_language":"English"
    
    },
    "studys":{
        
        "school":[
            "school_number_3",
            "isito"
        ],
        
        "university":"KGTU name of Razzakova",
        
        "courses":[
            
            "engish_course - Enlish Zone",
            "programming_course-IT academy",
            "tehnologys_course-Alma-Ata,Kazakstan"
        ]
    },

    "family": [
        "two brothers",
        "Mommy"
    ],
    
    "hobbys": [
        "Guitar",
        "Chess",
        "Programming",
        "Soccer"
    ]
    

}

save_information_about_me = []
save_information_about_me.append(personal_information_of_me)
json.dump(save_information_about_me,my_file,sort_keys=False, indent=4)
my_file.close()