import streamlit as st
import requests
import json
from datetime import datetime
# API Endpoint
#API_URL = "https://your-api-endpoint.com/process"  # Replace with your actual API URL

from datetime import datetime
from dateutil.relativedelta import relativedelta

BANK_RULES = {
    "HERO": {
        "cibil_score": [
            (300, 650, "PASS"), (651, 699, "PASS"), (700, 719, "PASS"),
            (720, 724, "PASS"), (725, 749, "PASS"), (750, float('inf'), "PASS")
        ],
        "cibil_enquiry_count": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, 10, "PASS"), (11, float('inf'), "PASS")
        ],
        "dpd_1_30": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_44": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "PASS")
        ],
        "dpd_1_above": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, float('inf'), "REJECT")
        ],
        "dpd_31_44": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, float('inf'), "REJECT")
        ],
        "dpd_45_above": [
            (0, 0, "PASS"), (1, float('inf'), "REJECT")
        ],
        "car_age": [
            (0, 84, "PASS"), (85, 96, "PASS"), (97, 108, "PASS"), (109, 120, "PASS"),
            (121, 132, "REJECT"), (133, 144, "REJECT"), (145, float('inf'), "REJECT")
        ],
        "car_owner_age": [
            (0, 21, "CHECK OTHER CONDITION"), (22, 25, "CHECK OTHER CONDITION"),
            (26, 28, "CHECK OTHER CONDITION"), (29, 30, "CHECK OTHER CONDITION"),
            (31, 53, "PASS"), (54, 70, "PASS"), (71, float('inf'), "CHECK OTHER CONDITION")
        ],
        "loan_amount": [
            (0, 100000, "PASS"), (100001, 500000, "REJECT"), (500001, float('inf'), "REJECT")
        ],
        "bounces_0_3_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, float('inf'), "REJECT")
        ],
        "bounces_0_6_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, 3, "PASS"), (4, float('inf'), "REJECT")
        ],
         "mother_0_3": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, 3, "PASS"), (4, float('inf'), "PASS")
        ],
        "mother_4_6": [
            (0, 0, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_7_12": [
            (0, 0, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_13_24": [
            (0, 0, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_25_60": [
            (0, 0, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_6": [
            (0, 0, "PASS"),(4, float('inf'), "PASS")
        ],
                "mother_0_9": [
            (0, 0, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_12": [
            (0, 0, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_24": [
            (0, 0, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_60": [
            (0, 0, "PASS"),(4, float('inf'), "PASS")
        ]

    },
    "IDFC": {
        "cibil_score": [
            (300, 650, "REJECT"), (651, 699, "PASS"), (700, 719, "PASS"),
            (720, 724, "PASS"), (725, 749, "PASS"), (750, float('inf'), "PASS")
        ],
        "cibil_enquiry_count": [
            (0, 0, "PASS"), (1, 6, "PASS"), (7, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_30": [
            (0, 0, "PASS"), (1, 6, "PASS"), (6, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_44": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "PASS")
        ],
        "dpd_1_above": [
            (0, 0, "PASS"), (1, 1, "PASS"), (6, float('inf'), "REJECT")
        ],
        "dpd_31_44": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, float('inf'), "REJECT")
        ],
        
        "dpd_45_above": [
            (0, 0, "PASS"), (1, float('inf'), "REJECT")
        ],
        "car_age": [
            (0, 84, "PASS"), (85, 96, "PASS"), (97, 108, "REJECT"), (109, 120, "REJECT"),
            (121, 132, "REJECT"), (133, 144, "REJECT"), (145, float('inf'), "REJECT")
        ],
        "car_owner_age": [
            (0, 21, "CHECK OTHER CONDITION"), (22, 25, "CHECK OTHER CONDITION"),
            (26, 28, "CHECK OTHER CONDITION"), (29, 30, "CHECK OTHER CONDITION"),
            (31, 53, "PASS"), (54, 70, "PASS"), (71, float('inf'), "CHECK OTHER CONDITION")
        ],
        "loan_amount": [
            (0, 100000, "PASS"), (100001, 500000, "REJECT"), (500001, float('inf'), "REJECT")
        ],
        "bounces_0_3_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "REJECT"), (3, float('inf'), "REJECT")
        ],
        "bounces_0_6_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, 3, "REJECT"), (4, float('inf'), "REJECT")
        ],
        "mother_0_3": [
            (0, 0, "PASS"), (1, 1, "REJECT"), (2, 2, "REJECT"), (3, float('inf'), "REJECT")
        ],
        "mother_4_6": [
            (0, 2, "PASS"),(3, float('inf'), "REJECT")
        ],
        "mother_7_12": [
            (0, 2, "PASS"),(3, float('inf'), "REJECT")
        ],
        "mother_13_24": [
            (0, 3, "PASS"),(4, float('inf'), "REJECT")
        ],
        "mother_25_60": [
            (0, 5, "PASS"),(6, float('inf'), "REJECT")
        ],
        "mother_0_6": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_9": [
            (0, 0, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_12": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_24": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_60": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ]
    },

    "TATA": {
        "cibil_score": [
            (300, 650, "REJECT"), (651, 699, "REJECT"), (700, 719, "PASS"),
            (720, 724, "PASS"), (725, 749, "PASS"), (750, float('inf'), "PASS")
        ],
        "cibil_enquiry_count": [
            (0, 0, "PASS"), (1, 5, "PASS"),(6,9,'PASS'), (10, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_30": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_44": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "REJECT")
        ],
        "dpd_1_above": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "PASS")
        ],
        "dpd_31_44": [
            (0, 0, "PASS"), (1, 4, "PASS"), (5, float('inf'), "REJECT")
        ],
        "dpd_45_above": [
            (0, 1, "PASS"), (2, float('inf'), "REJECT")
        ],
        "car_age": [
            (0, 84, "PASS"), (85, 96, "PASS"), (97, 108, "REJECT"), (109, 120, "REJECT"),
            (121, 132, "REJECT"), (133, 144, "REJECT"), (145, float('inf'), "REJECT")
        ],
        "car_owner_age": [
            (0, 21, "CHECK OTHER CONDITION"), (22, 25, "CHECK OTHER CONDITION"),
            (26, 28, "CHECK OTHER CONDITION"), (29, 30, "CHECK OTHER CONDITION"),
            (31, 53, "PASS"), (54, 70, "PASS"), (71, float('inf'), "CHECK OTHER CONDITION")
        ],
        "loan_amount": [
            (0, 100000, "PASS"), (100001, 500000, "REJECT"), (500001, float('inf'), "REJECT")
        ],
        "bounces_0_3_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, float('inf'), "REJECT")
        ],
        "bounces_0_6_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, 3, "PASS"), (4, float('inf'), "REJECT")
        ],
                "mother_0_3": [
            (0, 0, "PASS"),(1, float('inf'), "REJECT")
        ],
        "mother_4_6": [
            (0, 2, "PASS"),(3, float('inf'), "REJECT")
        ],
        "mother_7_12": [
            (0, 2, "PASS"),(3, float('inf'), "REJECT")
        ],
        "mother_13_24": [
            (0, 3, "PASS"),(4, float('inf'), "REJECT")
        ],
        "mother_25_60": [
            (0, 5, "PASS"),(6, float('inf'), "REJECT")
        ],
        "mother_0_6": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_9": [
            (0, 0, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_12": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_24": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_60": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ]
    },

      "BAJAJ": {
        "cibil_score": [
            (300, 650, "REJECT"), (651, 699, "REJECT"), (700, 719, "REJECT"),
            (720, 724, "PASS"), (725, 749, "PASS"), (750, float('inf'), "PASS")
        ],
        "cibil_enquiry_count": [
            (0, 0, "PASS"), (1, 6, "PASS"),(7,7,'REJECT'), (8, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_30": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_44": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "PASS")
        ],
        "dpd_1_above": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "PASS")
        ],
        "dpd_31_44": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_45_above": [
            (0, 0, "PASS"), (1, float('inf'), "REJECT")
        ],
        "car_age": [
            (0, 84, "PASS"), (85, 96, "CHECK OTHER CONDITION"), (97, 108, "CHECK OTHER CONDITION"), (109, 120, "REJECT"),
            (121, 132, "REJECT"), (133, 144, "REJECT"), (145, float('inf'), "REJECT")
        ],
        "car_owner_age": [
            (0, 21, "CHECK OTHER CONDITION"), (22, 25, "CHECK OTHER CONDITION"),
            (26, 28, "CHECK OTHER CONDITION"), (29, 30, "CHECK OTHER CONDITION"),
            (31, 53, "PASS"), (54, 70, "PASS"), (71, float('inf'), "CHECK OTHER CONDITION")
        ],
        "loan_amount": [
            (0, 100000, "PASS"), (100001, 500000, "REJECT"), (500001, float('inf'), "REJECT")
        ],
        "bounces_0_3_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "REJECT"), (3, float('inf'), "REJECT")
        ],
        "bounces_0_6_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, 3, "REJECT"), (4, float('inf'), "REJECT")
        ],
        "mother_0_3": [
            (0, 0, "PASS"),(1, float('inf'), "REJECT")
        ],
        "mother_4_6": [
            (0, 2, "PASS"),(3, float('inf'), "REJECT")
        ],
        "mother_7_12": [
            (0, 2, "PASS"),(3, float('inf'), "REJECT")
        ],
        "mother_13_24": [
            (0, 3, "PASS"),(4, float('inf'), "REJECT")
        ],
        "mother_25_60": [
            (0, 5, "PASS"),(6, float('inf'), "REJECT")
        ],
        "mother_0_6": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_9": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_12": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_24": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_60": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ]
    },
    "AXIS": {
        "cibil_score": [
            (300, 650, "PASS"), (651, 699, "PASS"), (700, 719, "PASS"),
            (720, 724, "PASS"), (725, 749, "PASS"), (750, float('inf'), "PASS")
        ],
       "cibil_enquiry_count": [
            (0, 0, "PASS"), (1, 5, "PASS"),(6,7,'PASS'), (6, 14, "PASS"), (15, float('inf'), "REJECT")
        ],
        "dpd_1_30": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, 10, "PASS"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_44": [
            (0, 0, "PASS"), (1, 5, "PASS"),(6,10,"PASS"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_above": [
            (0, 0, "PASS"), (1, 9, "PASS"), (10, float('inf'), "REJECT")
        ],
        "dpd_31_44": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, 10, "PASS"), (11, float('inf'), "PASS")
        ],
        "dpd_45_above": [
            (0, 1, "PASS"), (2, float('inf'), "REJECT")
        ],
        "car_age": [
            (0, 84, "PASS"), (85, 96, "PASS"), (97, 108, "REJECT"), (109, 120, "REJECT"),
            (121, 132, "REJECT"), (133, 144, "REJECT"), (145, float('inf'), "REJECT")
        ],
        "car_owner_age": [
            (0, 21, "CHECK OTHER CONDITION"), (22, 25, "CHECK OTHER CONDITION"),
            (26, 28, "CHECK OTHER CONDITION"), (29, 30, "CHECK OTHER CONDITION"),
            (31, 53, "PASS"), (54, 70, "PASS"), (71, float('inf'), "CHECK OTHER CONDITION")
        ],
        "loan_amount": [
            (0, 100000, "PASS"), (100001, 500000, "REJECT"), (500001, float('inf'), "REJECT")
        ],
        "bounces_0_3_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, float('inf'), "REJECT")
        ],
        "bounces_0_6_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, 3, "PASS"), (4, float('inf'), "REJECT")
        ],
        "mother_0_3": [
            (0, 2, "PASS"),(3, float('inf'), "REJECT")
        ],
        "mother_4_6": [
            (0, 2, "PASS"),(3, float('inf'), "PASS")
        ],
        "mother_7_12": [
            (0, 2, "PASS"),(3, float('inf'), "PASS")
        ],
        "mother_13_24": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_25_60": [
            (0, 5, "PASS"),(6, float('inf'), "PASS")
        ],
        "mother_0_6": [
            (0, 3, "PASS"),(4, float('inf'), "REJECT")
        ],
        "mother_0_9": [
            (0, 3, "PASS"),(4, float('inf'), "REJECT")
        ],
        "mother_0_12": [
            (0, 3, "PASS"),(4, float('inf'), "REJECT")
        ],
        "mother_0_24": [
            (0, 3, "PASS"),(5, float('inf'), "REJECT")
        ],
        "mother_0_60": [
            (0, 3, "PASS"),(8, float('inf'), "REJECT")
        ]

    },
     "YES BANK": {
        "cibil_score": [
            (300, 650, "REJECT"), (651, 699, "REJECT"), (700, 719, "PASS"),
            (720, 724, "PASS"), (725, 749, "PASS"), (750, float('inf'), "PASS")
        ],
       "cibil_enquiry_count": [
            (0, 0, "PASS"), (1, 6, "PASS"),(7,7,'REJECT'), (8, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_30": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_44": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "PASS")
        ],
        "dpd_1_above": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "REJECT")
        ],
        "dpd_31_44": [
            (0, 0, "PASS"), (1, 1, "PASS"),(2, float('inf'), "REJECT")
        ],

        "dpd_45_above": [
            (0, 0, "PASS"), (1, float('inf'), "REJECT")
        ],
        "car_age": [
            (0, 84, "PASS"), (85, 96, "REJECT"), (97, 108, "REJECT"), (109, 120, "REJECT"),
            (121, 132, "REJECT"), (133, 144, "REJECT"), (145, float('inf'), "REJECT")
        ],
        "car_owner_age": [
            (0, 21, "CHECK OTHER CONDITION"), (22, 25, "CHECK OTHER CONDITION"),
            (26, 28, "CHECK OTHER CONDITION"), (29, 30, "CHECK OTHER CONDITION"),
            (31, 53, "PASS"), (54, 70, "PASS"), (71, float('inf'), "CHECK OTHER CONDITION")
        ],
        "loan_amount": [
            (0, 100000, "PASS"), (100001, 500000, "REJECT"), (500001, float('inf'), "REJECT")
        ],
        "bounces_0_3_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "REJECT"), (3, float('inf'), "REJECT")
        ],
        "bounces_0_6_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, 3, "REJECT"), (4, float('inf'), "REJECT")
        ],
        "mother_0_3": [
            (0, 0, "PASS"),(1, float('inf'), "REJECT")
        ],
        "mother_4_6": [
            (0, 0, "PASS"),(1, float('inf'), "REJECT")
        ],
        "mother_7_12": [
            (0, 2, "PASS"),(3, float('inf'), "REJECT")
        ],
        "mother_13_24": [
            (0, 3, "PASS"),(4, float('inf'), "REJECT")
        ],
        "mother_25_60": [
            (0, 5, "PASS"),(6, float('inf'), "REJECT")
        ],
        "mother_0_6": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_9": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_12": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_24": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_60": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ]
    },
     "PIRAMAL": {
        "cibil_score": [
            (300, 650, "PASS"), (651, 699, "PASS"), (700, 719, "PASS"),
            (720, 724, "PASS"), (725, 749, "PASS"), (750, float('inf'), "PASS")
        ],
       "cibil_enquiry_count": [
            (0, 0, "PASS"), (1, 5, "PASS"),(6,7,'PASS'), (6, 10, "PASS"), (11, float('inf'), "PASS")
        ],
        "dpd_1_30": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_44": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "PASS")
        ],
        "dpd_1_above": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "REJECT")
        ],
        "dpd_31_44": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_45_above": [
            (0, 0, "PASS"), (1, float('inf'), "REJECT")
        ],
        "car_age": [
            (0, 84, "PASS"), (85, 96, "PASS"), (97, 108, "PASS"), (109, 120, "REJECT"),
            (121, 132, "REJECT"), (133, 144, "REJECT"), (145, float('inf'), "REJECT")
        ],
        "car_owner_age": [
            (0, 21, "CHECK OTHER CONDITION"), (22, 25, "CHECK OTHER CONDITION"),
            (26, 28, "CHECK OTHER CONDITION"), (29, 30, "CHECK OTHER CONDITION"),
            (31, 53, "PASS"), (54, 70, "PASS"), (71, float('inf'), "CHECK OTHER CONDITION")
        ],
        "loan_amount": [
            (0, 100000, "PASS"), (100001, 500000, "REJECT"), (500001, float('inf'), "REJECT")
        ],
        "bounces_0_3_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, float('inf'), "REJECT")
        ],
        "bounces_0_6_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, 3, "PASS"), (4, float('inf'), "REJECT")
        ],
        "mother_0_3": [
            (0, 0, "PASS"),(1, float('inf'), "REJECT")
        ],
        "mother_4_6": [
            (0, 2, "PASS"),(3, float('inf'), "REJECT")
        ],
        "mother_7_12": [
            (0, 3, "PASS"),(4, float('inf'), "REJECT")
        ],
        "mother_13_24": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_25_60": [
            (0, 5, "PASS"),(6, float('inf'), "PASS")
        ],
        "mother_0_6": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_9": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_12": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_24": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_60": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ]
    },
     "HDFC": {
        "cibil_score": [
            (300, 650, "REJECT"), (651, 699, "PASS"), (700, 719, "PASS"),
            (720, 724, "PASS"), (725, 749, "PASS"), (750, float('inf'), "PASS")
        ],
       "cibil_enquiry_count": [
            (0, 0, "PASS"), (1, 6, "PASS"),(7,7,'REJECT'), (8, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_30": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_44": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "PASS")
        ],
        "dpd_1_above": [
            (0, 5, "PASS"), (1, 5, "PASS"), (6, float('inf'), "REJECT")
        ],
        "dpd_31_44": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_45_above": [
            (0, 0, "PASS"), (1, float('inf'), "REJECT")
        ],
        "car_age": [
            (0, 84, "PASS"), (85, 96, "REJECT"), (97, 108, "REJECT"), (109, 120, "REJECT"),
            (121, 132, "REJECT"), (133, 144, "REJECT"), (145, float('inf'), "REJECT")
        ],
        "car_owner_age": [
            (0, 21, "CHECK OTHER CONDITION"), (22, 25, "CHECK OTHER CONDITION"),
            (26, 28, "CHECK OTHER CONDITION"), (29, 30, "CHECK OTHER CONDITION"),
            (31, 53, "PASS"), (54, 70, "PASS"), (71, float('inf'), "CHECK OTHER CONDITION")
        ],
        "loan_amount": [
            (0, 100000, "PASS"), (100001, 500000, "REJECT"), (500001, float('inf'), "REJECT")
        ],
        "bounces_0_3_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "REJECT"), (3, float('inf'), "REJECT")
        ],
        "bounces_0_6_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, 3, "REJECT"), (4, float('inf'), "REJECT")
        ],
        "mother_0_3": [
            (0, 1, "PASS"),(2, float('inf'), "REJECT")
        ],
        "mother_4_6": [
            (0, 2, "PASS"),(3, float('inf'), "PASS")
        ],
        "mother_7_12": [
            (0, 2, "PASS"),(3, float('inf'), "PASS")
        ],
        "mother_13_24": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_25_60": [
            (0, 5, "PASS"),(6, float('inf'), "PASS")
        ],
        "mother_0_6": [
            (0, 1, "PASS"),(2, float('inf'), "REJECT")
        ],
        "mother_0_9": [
            (0, 1, "PASS"),(2, float('inf'), "REJECT")
        ],
        "mother_0_12": [
            (0, 1, "PASS"),(2, float('inf'), "REJECT")
        ],
        "mother_0_24": [
            (0, 2, "PASS"),(3, float('inf'), "REJECT")
        ],
        "mother_0_60": [
            (0, 4, "PASS"),(5, float('inf'), "REJECT")
        ]
    },
    "ICICI": {
        "cibil_score": [
            (300, 650, "REJECT"), (651, 699, "REJECT"), (700, 719, "REJECT"),
            (720, 724, "PASS"), (725, 749, "PASS"), (750, float('inf'), "PASS")
        ],
       "cibil_enquiry_count": [
            (0, 0, "PASS"), (1, 6, "PASS"),(7,7,'REJECT'), (8, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_30": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_44": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "PASS")
        ],
        "dpd_1_above": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "REJECT")
        ],
        "dpd_31_44": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_45_above": [
            (0, 0, "PASS"), (1, float('inf'), "REJECT")
        ],
        "car_age": [
            (0, 84, "PASS"), (85, 96, "PASS"), (97, 108, "REJECT"), (109, 120, "REJECT"),
            (121, 132, "REJECT"), (133, 144, "REJECT"), (145, float('inf'), "REJECT")
        ],
        "car_owner_age": [
            (0, 21, "CHECK OTHER CONDITION"), (22, 25, "CHECK OTHER CONDITION"),
            (26, 28, "CHECK OTHER CONDITION"), (29, 30, "CHECK OTHER CONDITION"),
            (31, 53, "PASS"), (54, 70, "PASS"), (71, float('inf'), "CHECK OTHER CONDITION")
        ],
        "loan_amount": [
            (0, 100000, "PASS"), (100001, 500000, "REJECT"), (500001, float('inf'), "REJECT")
        ],
        "bounces_0_3_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, float('inf'), "REJECT")
        ],
        "bounces_0_6_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, 3, "PASS"), (4, float('inf'), "REJECT")
        ],
        "mother_0_3": [
            (0, 0, "PASS"),(1, float('inf'), "REJECT")
        ],
        "mother_4_6": [
            (0, 2, "PASS"),(3, float('inf'), "REJECT")
        ],
        "mother_7_12": [
            (0, 2, "PASS"),(3, float('inf'), "REJECT")
        ],
        "mother_13_24": [
            (0, 3, "PASS"),(4, float('inf'), "REJECT")
        ],
        "mother_25_60": [
            (0, 5, "PASS"),(6, float('inf'), "REJECT")
        ],
        "mother_0_6": [
            (0, 3, "PASS"),(4, float('inf'), "REJECT")
        ],
        "mother_0_9": [
            (0, 3, "PASS"),(4, float('inf'), "REJECT")
        ],
        "mother_0_12": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_24": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_60": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ]
    },
    "POONAWALA": {
        "cibil_score": [
            (300, 650, "REJECT"), (651, 699, "REJECT"), (700, 719, "PASS"),
            (720, 724, "PASS"), (725, 749, "PASS"), (750, float('inf'), "PASS")
        ],
       "cibil_enquiry_count": [
            (0, 0, "PASS"), (1, 5, "PASS"),(6,10,'PASS'), (11, 11, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_30": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_44": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "PASS")
        ],
        "dpd_1_above": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "REJECT")
        ],
        "dpd_31_44": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_45_above": [
            (0, 0, "PASS"), (1, float('inf'), "REJECT")
        ],
        "car_age": [
            (0, 84, "PASS"), (85, 96, "PASS"), (97, 108, "PASS"), (109, 120, "PASS"),
            (121, 132, "REJECT"), (133, 144, "REJECT"), (145, float('inf'), "REJECT")
        ],
        "car_owner_age": [
            (0, 21, "CHECK OTHER CONDITION"), (22, 25, "CHECK OTHER CONDITION"),
            (26, 28, "CHECK OTHER CONDITION"), (29, 30, "CHECK OTHER CONDITION"),
            (31, 53, "PASS"), (54, 70, "PASS"), (71, float('inf'), "CHECK OTHER CONDITION")
        ],
        "loan_amount": [
            (0, 100000, "PASS"), (100001, 500000, "REJECT"), (500001, float('inf'), "REJECT")
        ],
        "bounces_0_3_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, float('inf'), "REJECT")
        ],
        "bounces_0_6_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, 3, "PASS"), (4, float('inf'), "REJECT")
        ],
        "mother_0_3": [
            (0, 1, "PASS"),(1, float('inf'), "REJECT")
        ],
        "mother_4_6": [
            (0, 2, "PASS"),(3, float('inf'), "REJECT")
        ],
        "mother_7_12": [
            (0, 2, "PASS"),(3, float('inf'), "REJECT")
        ],
        "mother_13_24": [
            (0, 3, "PASS"),(4, float('inf'), "REJECT")
        ],
        "mother_25_60": [
            (0, 5, "PASS"),(6, float('inf'), "REJECT")
        ],
        "mother_0_6": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_9": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_12": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_24": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_60": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ]
    },
    "AU": {
        "cibil_score": [
            (300, 650, "PASS"), (651, 699, "PASS"), (700, 719, "PASS"),
            (720, 724, "PASS"), (725, 749, "PASS"), (750, float('inf'), "PASS")
        ],
       "cibil_enquiry_count": [
            (0, 0, "PASS"), (1, 5, "PASS"),(6,7,'PASS'), (6, 10, "PASS"), (11, float('inf'), "PASS")
        ],
        "dpd_1_30": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, 9, "PASS"), (10, float('inf'), "REJECT")
        ],
                "dpd_1_44": [
            (0, 0, "PASS"), (1, 9, "PASS"), (10, float('inf'), "REJECT")
        ],
        "dpd_1_above": [
            (0, 0, "PASS"), (1, 9, "PASS"), (10, float('inf'), "REJECT")
        ],
        "dpd_31_44": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, 10, "PASS"), (11, float('inf'), "PASS")
        ],
        "dpd_45_above": [
            (0, 0, "PASS"), (1, float('inf'), "PASS")
        ],
        "car_age": [
            (0, 84, "PASS"), (85, 96, "PASS"), (97, 108, "PASS"), (109, 120, "PASS"),
            (121, 132, "PASS"), (133, 144, "PASS"), (145, float('inf'), "PASS")
        ],
        "car_owner_age": [
            (0, 21, "CHECK OTHER CONDITION"), (22, 25, "CHECK OTHER CONDITION"),
            (26, 28, "CHECK OTHER CONDITION"), (29, 30, "CHECK OTHER CONDITION"),
            (31, 53, "PASS"), (54, 70, "PASS"), (71, float('inf'), "CHECK OTHER CONDITION")
        ],
        "loan_amount": [
            (0, 100000, "PASS"), (100001, 500000, "REJECT"), (500001, float('inf'), "REJECT")
        ],
        "bounces_0_3_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, float('inf'), "REJECT")
        ],
        "bounces_0_6_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, 3, "PASS"), (4, float('inf'), "REJECT")
        ],
        "mother_0_3": [
            (0, 0, "PASS"),(1, float('inf'), "PASS")
        ],
        "mother_4_6": [
            (0, 2, "PASS"),(3, float('inf'), "PASS")
        ],
        "mother_7_12": [
            (0, 2, "PASS"),(3, float('inf'), "PASS")
        ],
        "mother_13_24": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_25_60": [
            (0, 5, "PASS"),(6, float('inf'), "PASS")
        ],
        "mother_0_6": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_9": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_12": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_24": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_60": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ]
    },
    "CHOLA": {
        "cibil_score": [
            (300, 650, "PASS"), (651, 699, "PASS"), (700, 719, "PASS"),
            (720, 724, "PASS"), (725, 749, "PASS"), (750, float('inf'), "PASS")
        ],
       "cibil_enquiry_count": [
            (0, 0, "PASS"), (1, 6, "PASS"),(7,7,'REJECT'), (8, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
        "dpd_1_30": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, 10, "REJECT"), (11, float('inf'), "REJECT")
        ],
                "dpd_1_44": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "REJECT")
        ],
                "dpd_1_above": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, float('inf'), "REJECT")
        ],
        "dpd_31_44": [
            (0, 0, "PASS"), (1, 5, "PASS"), (6, 10, "PASS"), (11, float('inf'), "PASS")
        ],
        "dpd_45_above": [
            (0, 0, "PASS"), (1, float('inf'), "PASS")
        ],
        "car_age": [
            (0, 84, "PASS"), (85, 96, "PASS"), (97, 108, "PASS"), (109, 120, "PASS"),
            (121, 132, "PASS"), (133, 144, "PASS"), (145, float('inf'), "PASS")
        ],
        "car_owner_age": [
            (0, 21, "CHECK OTHER CONDITION"), (22, 25, "CHECK OTHER CONDITION"),
            (26, 28, "CHECK OTHER CONDITION"), (29, 30, "CHECK OTHER CONDITION"),
            (31, 53, "PASS"), (54, 70, "PASS"), (71, float('inf'), "CHECK OTHER CONDITION")
        ],
        "loan_amount": [
            (0, 100000, "PASS"), (100001, 500000, "REJECT"), (500001, float('inf'), "REJECT")
        ],
        "bounces_0_3_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, float('inf'), "REJECT")
        ],
        "bounces_0_6_months": [
            (0, 0, "PASS"), (1, 1, "PASS"), (2, 2, "PASS"), (3, 3, "PASS"), (4, float('inf'), "REJECT")
        ],
        "mother_0_3": [
            (0, 0, "PASS"),(1, float('inf'), "PASS")
        ],
        "mother_4_6": [
            (0, 2, "PASS"),(3, float('inf'), "PASS")
        ],
        "mother_7_12": [
            (0, 2, "PASS"),(3, float('inf'), "PASS")
        ],
        "mother_13_24": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_25_60": [
            (0, 5, "PASS"),(6, float('inf'), "PASS")
        ],
        "mother_0_6": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_9": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_12": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_24": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ],
        "mother_0_60": [
            (0, 3, "PASS"),(4, float('inf'), "PASS")
        ]
    },



}




def find_mother_auto_loan(data, data_car):
    registration_date_str = data_car["data"].get("registration_date")
    if not registration_date_str:
        return None

    registration_date = datetime.strptime(registration_date_str, "%Y-%m-%d")
    valid_months = {
        (registration_date - relativedelta(months=i)).strftime("%Y-%m")
        for i in range(3)
    }

    accounts = data.get("data", {}).get("credit_report", [{}])[0].get("accounts", [])

    for account in accounts:
        account_type = account.get("accountType", "").lower()
        date_opened = account.get("dateOpened")

        if not date_opened or ("auto" not in account_type and "car" not in account_type):
            continue

        try:
            loan_open_month = datetime.strptime(date_opened, "%Y-%m-%d").strftime("%Y-%m")
            if loan_open_month in valid_months:
                return account  # Return the full account for further use
        except ValueError:
            continue

    return None

def calculate_bounce_ranges(account, as_of_date=None):
    if as_of_date is None:
        as_of_date = datetime.today()

    monthly_statuses = account.get("monthlyPayStatus", [])
    dpd_records = [
        (datetime.strptime(entry["date"], "%Y-%m-%d"), entry["status"])
        for entry in monthly_statuses
        if "status" in entry and entry["status"].isdigit() and int(entry["status"]) > 0
    ]

    # Define bucket ranges
    buckets = {
        "0_3": 3,
        "4_6": 6,
        "7_12": 12,
        "13_24": 24,
        "25_60": 60,
    }

    bounce_summary = {
        "0_3": 0, "4_6": 0, "7_12": 0, "13_24": 0, "25_60": 0,
        "0_6": 0, "0_9": 0, "0_12": 0, "0_24": 0, "0_60": 0
    }

    for dpd_date, status in dpd_records:
        month_diff = (as_of_date.year - dpd_date.year) * 12 + (as_of_date.month - dpd_date.month)

        if month_diff < 0 or month_diff > 60:
            continue

        if month_diff <= 2:
            bounce_summary["0_3"] += 1
        elif 3 <= month_diff <= 5:
            bounce_summary["4_6"] += 1
        elif 6 <= month_diff <= 11:
            bounce_summary["7_12"] += 1
        elif 12 <= month_diff <= 23:
            bounce_summary["13_24"] += 1
        elif 24 <= month_diff <= 59:
            bounce_summary["25_60"] += 1

        # Ranges
        if month_diff <= 5:
            bounce_summary["0_6"] += 1
        if month_diff <= 8:
            bounce_summary["0_9"] += 1
        if month_diff <= 11:
            bounce_summary["0_12"] += 1
        if month_diff <= 23:
            bounce_summary["0_24"] += 1
        bounce_summary["0_60"] += 1  # Always include if within 60 months

    return bounce_summary
def format_bounce_summary(bounce_summary):
    labels = {
        "0_3": "Last 0–3 months",
        "4_6": "Last 4–6 months",
        "7_12": "Last 7–12 months",
        "13_24": "Last 13–24 months",
        "25_60": "Last 25–60 months",
        "0_6": "Last 0–6 months",
        "0_9": "Last 0–9 months",
        "0_12": "Last 0–12 months",
        "0_24": "Last 0–24 months",
        "0_60": "Last 0–60 months"
    }

    formatted = "\nBounce Summary:\n"
    for key in labels:
        formatted += f"• {labels[key]}: {bounce_summary.get(key, 0)} DPDs\n"

    return formatted

def check_condition(value, rules):
    """
    Check if a given value satisfies any of the conditions in the rules.
    """
    for rule in rules:
        min_val, max_val, result = rule
        if min_val <= value <= max_val:
            return result
    return "Invalid"


def evaluate_loan_eligibility(bank_name, cibil_score, enquiry_count, dpd_1_30, dpd_1_44,dpd_1_above, dpd_31_44, dpd_45_above,
                              car_age, car_owner_age, bounces_0_3, bounces_0_6,mother_0_3,mother_4_6,mother_7_12,mother_13_24,mother_25_60,mother_0_6,mother_0_9,mother_0_12,mother_0_24,mother_0_60):
    """
    Evaluate loan eligibility based on rules.
    Returns:
        - 'Eligible for Loan' if all pass
        - List of rejection reasons like 'DPD 45 Above: 2' (i.e., field: value)
    """
    bank_rules = BANK_RULES.get(bank_name)
    if not bank_rules:
        return ["Bank not supported"]
   
    checks = {
        "CIBIL Score": (cibil_score, bank_rules["cibil_score"]),
        "CIBIL Enquiry Count": (enquiry_count, bank_rules["cibil_enquiry_count"]),
        "DPD 1-30": (dpd_1_30, bank_rules["dpd_1_30"]),
        "DPD 1-44": (dpd_1_44, bank_rules["dpd_1_44"]),
        "DPD 1-Above": (dpd_1_above, bank_rules["dpd_1_above"]),
        "DPD 31-44": (dpd_31_44, bank_rules["dpd_31_44"]),
        "DPD 45 Above": (dpd_45_above, bank_rules["dpd_45_above"]),
        "Car Age": (car_age, bank_rules["car_age"]),
        "Car Owner Age": (car_owner_age, bank_rules["car_owner_age"]),
        "other Bounces 0-3 Months": (bounces_0_3, bank_rules["bounces_0_3_months"]),
        "other Bounces 0-6 Months": (bounces_0_6, bank_rules["bounces_0_6_months"]),
        "Bounces mother auto loan 0-3 months":(mother_0_3,bank_rules["mother_0_3"]),
        "Bounces mother auto loan 4-6 months":(mother_4_6,bank_rules["mother_4_6"]),
        "Bounces mother auto loan 7-12 months":(mother_7_12,bank_rules["mother_7_12"]),
        "Bounces mother auto loan 13-24 months":(mother_13_24,bank_rules["mother_13_24"]),
        "Bounces mother auto loan 25-60 months":(mother_25_60,bank_rules["mother_25_60"]),
        "Bounces mother auto loan 0-6 months":(mother_0_6,bank_rules["mother_0_6"]),
        "Bounces mother auto loan 0-9 months":(mother_0_9,bank_rules["mother_0_9"]),
        "Bounces mother auto loan 0-12 months":(mother_0_12,bank_rules["mother_0_12"]),
        "Bounces mother auto loan 0-24 months":(mother_0_24,bank_rules["mother_0_24"]),
        "Bounces mother auto loan 0-60 months":(mother_0_60,bank_rules["mother_0_60"])
            
        }

    rejection_reasons = []

    for key, (value, rule) in checks.items():
        if check_condition(value, rule) == "REJECT":
            rejection_reasons.append(f"{key}: {value}")  # Only include field and its value

    if rejection_reasons:
        return rejection_reasons
    else:
        return "Eligible for Loan"







# Function to parse DPD from paymentHistory
def parse_dpd(payment_history, months_to_check=7):
    # Each DPD entry is 3 characters, reverse to get latest first
    dpd_entries = [payment_history[i:i+3] for i in range(0, len(payment_history), 3)][::-1]
    # Take only the most recent 'months_to_check' entries
    return dpd_entries[:min(months_to_check, len(dpd_entries))]

# Function to check if DPD indicates a bounce (DPD > 0)
def is_bounce(dpd_str):
    try:
        dpd = int(dpd_str)
        return dpd > 0
    except ValueError:
        return False  # Skip non-numeric entries like "DBT" or "XXX"

# Function to parse DPD from paymentHistory
def parse_dpd(payment_history, months_to_check=4):
    # Each DPD entry is 3 characters, reverse to get latest first
    dpd_entries = [payment_history[i:i+3] for i in range(0, len(payment_history), 3)][::-1]
    # Take only the most recent 'months_to_check' entries
    return dpd_entries[:min(months_to_check, len(dpd_entries))]

# Function to check if DPD indicates a bounce (DPD > 0)
def is_bounce(dpd_str):
    try:
        dpd = int(dpd_str)
        return dpd > 0
    except ValueError:
        return False  # Skip non-numeric entries like "DBT" or "XXX"

def parse_dpd(payment_history, months_to_check=13):
    # Each DPD entry is 3 characters, reverse to get latest first
    dpd_entries = [payment_history[i:i+3] for i in range(0, len(payment_history), 3)][::-1]
    # Take only the most recent 'months_to_check' entries
    return dpd_entries[:min(months_to_check, len(dpd_entries))]

# Function to check if DPD is between 1 and 45 days
def is_dpd_1_to_45(dpd_str):
    try:
        dpd = int(dpd_str)
        return 1 <= dpd <= 45
    except ValueError:
        return False  # Skip non-numeric entries like "DBT" or "XXX"
def get_field(field_path):
    current = data
    for key in field_path.split('.'):
        if isinstance(current, dict):
            current = current.get(key)
        elif isinstance(current, list) and key.isdigit():
            current = current[int(key)]
        else:
            return None
    return current

def load_and_print_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        print("JSON Data from file:")
        print(json.dumps(data, indent=4))
        return data

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{file_path}' is not a valid JSON file.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Function to parse DPD from paymentHistory
def parse_dpd(payment_history, months_to_check=13):
    # Each DPD entry is 3 characters, reverse to get latest first
    dpd_entries = [payment_history[i:i+3] for i in range(0, len(payment_history), 3)][::-1]
    # Take only the most recent 'months_to_check' entries
    return dpd_entries[:min(months_to_check, len(dpd_entries))]

# Function to check if DPD is between 1 and 30 days
def is_dpd_1_to_30(dpd_str):
    try:
        dpd = int(dpd_str)
        return 1 <= dpd <= 30
    except ValueError:
        return False  # Skip non-numeric entries like "DBT" or "XXX"


def count_dpd_1_30_last_12_months(data):
    valid_account_types = {"AL", "TW", "PL", "BL", "HL", "LAP", "CVL"}
    today = datetime.today()

    # Start from the 1st of the same month last year
    start_date = (today.replace(day=1) - relativedelta(months=12))
    end_date = today  # Include current date

    count = 0

    for account in data.get("data", {}).get("credit_report", [])[0].get("accounts", []):
        if account.get("account_type") not in valid_account_types:
            continue

        for dpd_record in account.get("dpd", []):
            dpd_days = dpd_record.get("dpd", 0)
            dpd_date_str = dpd_record.get("date")
            if not dpd_date_str:
                continue

            try:
                dpd_date = datetime.strptime(dpd_date_str, "%Y-%m-%d")
            except ValueError:
                continue

            if 1 <= dpd_days <= 30 and start_date <= dpd_date <= end_date:
                count += 1

    return count

def count_dpd_1_45_last_12_months(data):
    valid_account_types = {"AL", "TW", "PL", "BL", "HL", "LAP", "CVL"}
    today = datetime.today()

    # Start from the 1st of the same month last year
    start_date = (today.replace(day=1) - relativedelta(months=12))
    end_date = today  # Current date

    count = 0

    for account in data.get("data", {}).get("credit_report", [])[0].get("accounts", []):
        if account.get("account_type") not in valid_account_types:
            continue

        for dpd_record in account.get("dpd", []):
            dpd_days = dpd_record.get("dpd", 0)
            dpd_date_str = dpd_record.get("date")
            if not dpd_date_str:
                continue

            try:
                dpd_date = datetime.strptime(dpd_date_str, "%Y-%m-%d")
            except ValueError:
                continue

            if 1 <= dpd_days <= 45 and start_date <= dpd_date <= end_date:
                count += 1

    return count

def count_dpd_45_plus_last_12_months(data):
    count = 0
    allowed_account_types = {"AL", "TW", "PL", "BL", "HL", "LAP", "CVL"}
    today = datetime.today()
    start_date = today - relativedelta(months=12)

    for account in data.get("data", {}).get("credit_report", [])[0].get("accounts", []):
        if account.get("account_type") not in allowed_account_types:
            continue

        for payment in account.get("payment_history", []):
            payment_date_str = payment.get("payment_date")
            dpd_days = payment.get("dpd", 0)

            if not payment_date_str:
                continue

            payment_date = datetime.strptime(payment_date_str, "%Y-%m-%d")

            if start_date <= payment_date <= today and dpd_days >= 45:
                count += 1

    return count


def count_dpd_31_44_last_12_months(data):
    count = 0
    allowed_account_types = {"AL", "TW", "PL", "BL", "HL", "LAP", "CVL"}
    today = datetime.today()
    start_date = today - relativedelta(months=12)

    for account in data.get("data", {}).get("credit_report", [])[0].get("accounts", []):
        if account.get("account_type") not in allowed_account_types:
            continue

        for payment in account.get("payment_history", []):
            payment_date_str = payment.get("payment_date")
            dpd_days = payment.get("dpd", 0)

            if not payment_date_str:
                continue

            payment_date = datetime.strptime(payment_date_str, "%Y-%m-%d")

            if start_date <= payment_date <= today and 31 <= dpd_days <= 44:
                count += 1

    return count

def count_dpd_45_above_last_12_months(data):
    today = datetime.today()
    start_date = (today - relativedelta(months=12)).replace(day=1)
    valid_account_types = {"AL", "TW", "PL", "BL", "HL", "LAP", "CVL"}
    count = 0

    for account in data["data"]["credit_report"][0]["accounts"]:
        acc_type = account.get("account_type")
        if acc_type in valid_account_types:
            for entry in account.get("payment_history", []):
                payment_date = datetime.strptime(entry["payment_date"], "%Y-%m-%d")
                if payment_date >= start_date:
                    dpd = entry.get("dpd", 0)
                    if dpd >= 45:
                        count += 1
    return count
def get_recent_bounces(data, current_date=None):
    print(current_date)
    # Set current date
    if current_date is None:
        current_date = datetime.today()
    else:
        current_date = datetime.strptime(current_date, "%Y-%m-%d")

    # Prepare the list of target months (current + last 3 months)
    recent_months = [(current_date - relativedelta(months=i)).strftime("%Y-%m") for i in range(4)]

    # Define valid account types
    valid_account_types = {"PL", "BL", "LAP", "AL", "CVL"}

    bounce_count = 0

    for account in data.get("accounts", []):
        acc_type = account.get("account_type", "").upper()
        if acc_type not in valid_account_types:
            continue

        for entry in account.get("payment_history", []):
            month = entry.get("month")
            dpd = entry.get("dpd", "000")
            status = entry.get("payment_status", "").upper()

            if month in recent_months:
                try:
                    dpd_int = int(dpd)
                except ValueError:
                    dpd_int = 0  # Treat invalid dpd as 0

                if dpd_int >= 30 or status == "DPD":
                    bounce_count += 1

    return bounce_count

def count_bounces_0_6_months(json_data):
    today = datetime.today()
    relevant_months = set()

    # Collect current + last 5 calendar months (total 6)
    for i in range(6):
        date = today - relativedelta(months=i)
        relevant_months.add((date.year, date.month))

    valid_account_types = {"PL", "BL", "LAP", "AL", "CVL"}
    total_bounces = 0

    accounts = json_data["data"]["credit_report"][0]["accounts"]

    for account in accounts:
        if account.get("account_type") in valid_account_types:
            for history in account.get("payment_history", []):
                month = history.get("month")
                year = history.get("year")
                payment_status = history.get("payment_status")

                if (year, month) in relevant_months and payment_status > 0:
                    total_bounces += 1

    return total_bounces


def count_bounces_0_12_months(json_data):
    today = datetime.today()
    relevant_months = set()

    # Collect current + last 11 calendar months (total 12)
    for i in range(12):
        date = today - relativedelta(months=i)
        relevant_months.add((date.year, date.month))

    valid_account_types = {"PL", "BL", "LAP", "AL", "CVL"}
    total_bounces = 0

    accounts = json_data["data"]["credit_report"][0]["accounts"]

    for account in accounts:
        if account.get("account_type") in valid_account_types:
            for history in account.get("payment_history", []):
                month = history.get("month")
                year = history.get("year")
                payment_status = history.get("payment_status")

                if (year, month) in relevant_months and payment_status > 0:
                    total_bounces += 1

    return total_bounces



from datetime import datetime
from dateutil.relativedelta import relativedelta

def count_bounces_by_period(data, current_date=None, exclude_account_number=None):
    if current_date is None:
        current_date = datetime.today()
    else:
        current_date = datetime.strptime(current_date, "%Y-%m-%d")

    # Prepare timeframes
    month_0_3 = current_date - relativedelta(months=3)
    month_0_6 = current_date - relativedelta(months=6)
    month_0_12 = current_date - relativedelta(months=12)

    bounces = {
        "bounces_0_3_months": 0,
        "bounces_0_6_months": 0,
        "bounces_0_12_months": 0
    }

    for account in data.get("data", {}).get("credit_report", [])[0].get("accounts", []):
        account_type = account.get("accountType", "").lower()
        account_number = account.get("accountNumber")

        if "loan" not in account_type:
            continue  # Filter only loan accounts

        # Skip the mother loan account
        if exclude_account_number and account_number == exclude_account_number:
            continue

        for record in account.get("monthlyPayStatus", []):
            date_str = record.get("date")
            status_str = record.get("status")

            if not date_str or not status_str or status_str.lower() == "xxx":
                continue

            try:
                dpd_date = datetime.strptime(date_str, "%Y-%m-%d")
                dpd = int(status_str)
            except (ValueError, TypeError):
                continue

            if dpd >= 30:
                if dpd_date >= month_0_12:
                    bounces["bounces_0_12_months"] += 1
                if dpd_date >= month_0_6:
                    bounces["bounces_0_6_months"] += 1
                if dpd_date >= month_0_3:
                    bounces["bounces_0_3_months"] += 1

    return bounces


def count_custom_dpd_buckets(data):
    today = datetime.today()
    start_date = (today.replace(day=1) - relativedelta(months=12))
    end_date = today

    dpd_counts = {
        "dpd_1_30": 0,
        "dpd_1_45": 0,
        "dpd_1_above": 0,
        "dpd_31_44": 0,
        "dpd_45_above": 0,
    }

    for account in data.get("data", {}).get("credit_report", [])[0].get("accounts", []):
        account_type = account.get("accountType", "").lower()

        # Consider only loan-type accounts (adjust as needed)
        
        if "loan" not in account_type:
            continue
        
        for record in account.get("monthlyPayStatus", []):
            date_str = record.get("date")
            status_str = record.get("status")

            if not date_str or not status_str or status_str.lower() == "xxx":
                continue

            try:
                dpd_date = datetime.strptime(date_str, "%Y-%m-%d")
                dpd_days = int(status_str)
            except (ValueError, TypeError):
                continue

            if start_date <= dpd_date <= end_date and dpd_days > 0:
                if 1 <= dpd_days <= 30:
                    dpd_counts["dpd_1_30"] += 1
                if 1 <= dpd_days <= 45:
                    dpd_counts["dpd_1_45"] += 1
                if dpd_days >= 1:
                    dpd_counts["dpd_1_above"] += 1
                if 31 <= dpd_days <= 44:
                    dpd_counts["dpd_31_44"] += 1
                if dpd_days >= 45:
                    dpd_counts["dpd_45_above"] += 1

    return dpd_counts

# Function to call the CIBIL API
def fetch_cibil_data(mobile, pan, name, gender, consent, token):
    url = "https://kyc-api.surepass.io/api/v1/credit-report-cibil/fetch-report"

    payload = {
        "mobile": mobile,
        "pan": pan,
        "name": name,
        "gender": gender.lower(),
        "consent": consent
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching CIBIL data: {e}")
        return None

# Function to call the Car API
def fetch_car_data(id_number, token):
    url = "https://kyc-api.surepass.io/api/v1/rc/rc-full"

    payload = {
        "id_number": id_number
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching car data: {e}")
        return None
# Streamlit Page Configuration
st.set_page_config(page_title="User Data Submission", layout="centered")

# UI Styling
st.markdown(
    """
    <style>
        .stTextInput, .stSelectbox, .stButton>button {
            font-size: 18px;
            padding: 10px;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            border-radius: 8px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Application Title
st.title("📱 User Data Submission Portal")

# UI Layout
st.markdown("### Please enter your details below:")

# User Input Form with Sidebar
with st.form("user_form"):
    mobile = st.text_input("📞 Mobile Number", "8554947999")
    pan = st.text_input("🆔 PAN", "AQUPN6092K")
    name = st.text_input("👤 Name", "Prasad Naik")
    gender = st.selectbox("⚧ Gender", ["Male", "Female", "Other"], index=0)
    id_number = st.text_input("🆔 Vehicle ID", "MH04KW6003")
    consent = st.selectbox("✔ Consent", ["Y", "N"], index=0)
    submit = st.form_submit_button("🚀 Submit")
# TOKEN for API authorization
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNDE3MTI4OCwianRpIjoiNDI0ZmM1ZmYtYzBmOC00YmYxLWE1MWQtMmVkYmMyN2Q4YjZhIiwidHlwZSI6ImFjY2VzcyIsImlkZW50aXR5IjoiZGV2LmJhZGFmaW5hbmNlX2NvbnNvbGVAc3VyZXBhc3MuaW8iLCJuYmYiOjE3MzQxNzEyODgsImV4cCI6MjM2NDg5MTI4OCwiZW1haWwiOiJiYWRhZmluYW5jZV9jb25zb2xlQHN1cmVwYXNzLmlvIiwidGVuYW50X2lkIjoibWFpbiIsInVzZXJfY2xhaW1zIjp7InNjb3BlcyI6WyJ1c2VyIl19fQ.md1Oaj19QbxeXmjyfdRMJMF50j9c9i_oPtX2UreFKKM"
# Send Data to API
if submit:
    with st.spinner("Processing..."):
        data = {
            "mobile": mobile,
            "pan": pan,
            "name": name,
            "gender": gender.lower(),
            "id_number": id_number,
            "consent": consent
        }
        
        try:

            data = fetch_cibil_data(mobile, pan, name, gender, consent, TOKEN)
            data_car = fetch_car_data(id_number, TOKEN)
            if data:
                st.success("CIBIL data fetched successfully!")
               #st.json(data)  # Optional: To show the JSON in UI

            if data_car:
               st.success("Car data fetched successfully!")
               #st.json(data_car)

#https://developers.kudosfinance.in/docs/list-of-cibil-field-input
            #file_path = "data8.json"
            #data = load_and_print_json(file_path)
            #        #  Example usage
            #file_path = "car8.json"
            #data_car = load_and_print_json(file_path)
            # Example usage (you'll ask for specific fields)
            name = get_field("data.name")  # Would print: Vishal Rathore
            credit_score = get_field("data.credit_score")  # Would print: 744
            # Define valid enquiryPurpose codes for PL, BL, LAP, CVL
            valid_purpose_codes = {"01","05","17","32","50","51","53","54","61"}
#1 ,5,17,32,50, 51, 53, 54,61
            # Get today's date
            today = datetime.today()

            # Define the start of the window (1st day of the month, 3 months ago)
            start_date = (today.replace(day=1) - relativedelta(months=3))

            # Initialize count
            enquiry_count = 0

            # Access enquiries from data
            enquiries = data["data"]["credit_report"][0].get("enquiries", [])

            for enquiry in enquiries:
                enquiry_date_str = enquiry.get("enquiryDate")  # date format: YYYY-MM-DD
                enquiry_purpose = enquiry.get("enquiryPurpose", "")

                if enquiry_date_str and enquiry_purpose in valid_purpose_codes:
                    try:
                        enquiry_date = datetime.strptime(enquiry_date_str, "%Y-%m-%d")
                        if enquiry_date >= start_date:
                            enquiry_count += 1
                    except ValueError:
                        print(f"Invalid date format: {enquiry_date_str}")

            print("Valid PL/BL/LAP/CVL enquiries in current + last 3 calendar months:", enquiry_count)
            print(name)
            print(credit_score)
            # Assuming json_data is your JSON object
            # Get the accounts list
            accounts = data["data"]["credit_report"][0]["accounts"]
          
            # Calculate total loan amount by summing highCreditAmount
            total_loan_amount = sum(int(account["highCreditAmount"]) for account in accounts)

            
            print(total_loan_amount)
            print(f"Total loan amount: {total_loan_amount}")


            # Get the registration date from the data
            registration_date_str = data_car["data"]["registration_date"]
            registration_date = datetime.strptime(registration_date_str, "%Y-%m-%d")

            # Use current system date dynamically
            current_date = datetime.today()

            # Calculate year and month differences
            year_diff = current_date.year - registration_date.year
            month_diff = current_date.month - registration_date.month

            # Total months
            total_months = (year_diff * 12) + month_diff

            # Adjust if the current day is before the registration day
            if current_date.day < registration_date.day:
                total_months -= 1

            print(f"Car Age in months: {total_months}")


            from datetime import datetime

            # Get the birth date from the CIBIL report
            birth_date_str = data["data"]["credit_report"][0]["names"][0]["birthDate"]
            birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")

            # Get current date in real-time
            current_date = datetime.today()

            # Calculate age in years
            year_diff = current_date.year - birth_date.year
            month_diff = current_date.month - birth_date.month
            day_diff = current_date.day - birth_date.day

            # Adjust if birthday hasn't occurred this year
            if month_diff < 0 or (month_diff == 0 and day_diff < 0):
                year_diff -= 1

            print(f"Car Owner Age (based on CIBIL birthDate): {year_diff} years")


           
            
            # Example usage
            dpd_summary = count_custom_dpd_buckets(data)
            print("Custom DPD Summary in Last 12 Months:", dpd_summary)
            mother_loan = find_mother_auto_loan(data, data_car)
            # Example usage
            # Get today's date in "YYYY-MM-DD" format
            current_date = datetime.today().strftime("%Y-%m-%d")

            # Extract mother loan account number if available
            exclude_account_number = mother_loan.get("accountNumber") if mother_loan else None

            print(exclude_account_number)
            print(current_date)
            bounces = count_bounces_by_period(data, current_date=current_date, exclude_account_number=exclude_account_number)
            print("Bounce Summary:")
            print(bounces)
            




            # Store individual values from summary dictionary into variables
            dpd_1_30_count = dpd_summary.get("dpd_1_30", 0)
            dpd_1_45_count = dpd_summary.get("dpd_1_45", 0)
            dpd_1_above = dpd_summary.get("dpd_1_above", 0)
            dpd_31_44_count = dpd_summary.get("dpd_31_44", 0)
            dpd_45_above = dpd_summary.get("dpd_45_above", 0)
            
            print("dpd 1-30",dpd_1_30_count)
            print("dpd 1-45",dpd_1_45_count)
            print("dpd 1 and above",dpd_1_above)
            print("dpd 31-45",dpd_31_44_count)
            print("dpd 45 and above",dpd_45_above)
            
            bounce_0_3 = bounces["bounces_0_3_months"]

            bounces_0_6 =  bounces["bounces_0_6_months"]


            
            #calculation of mother auto loan
            
            mother_0_3 =    0
            mother_4_6 =0
            mother_7_12 = 0
            mother_13_24 = 0
            mother_25_60 = 0
            mother_0_6 =0
            mother_0_9 =0
            mother_0_12 = 0
            mother_0_24 = 0
            mother_0_60 = 0
            if mother_loan:
                bounces = calculate_bounce_ranges(mother_loan)
                print("✅ Mother Loan Found")
                print("Account Number:", mother_loan["accountNumber"])
                print("Bank:", mother_loan.get("memberShortName", "Unknown"))
                print("Loan Opened On:", mother_loan.get("dateOpened", "N/A"))
                print(format_bounce_summary(bounces))
                mother_0_3 = bounces["0_3"]
                mother_4_6 = bounces["4_6"]
                mother_7_12 = bounces["7_12"]
                mother_13_24 = bounces["13_24"]
                mother_25_60 = bounces["25_60"]
                mother_0_6 = bounces["0_6"]
                mother_0_9 = bounces["0_9"]
                mother_0_12 = bounces["0_12"]
                mother_0_24 = bounces["0_24"]
                mother_0_60 = bounces["0_60"]
            else:
                print("❌ No matching Auto/Car loan found.")
            
            

            

            banks = ['HERO', 'TATA', 'BAJAJ','IDFC', 'YES BANK', 'PIRAMAL', 'HDFC', 'ICICI', 'POONAWALA', 'AU', 'CHOLA','AXIS']

            accepted_banks = []
            rejected_banks = {}

            for bank in banks:
                result = evaluate_loan_eligibility(
                    bank, 
                    int(credit_score), 
                    int(enquiry_count), 
                    int(dpd_1_30_count), 
                    int(dpd_1_45_count),
                    int(dpd_1_above),
                    int(dpd_31_44_count),
                    int(dpd_45_above),
                    int(total_months), 
                    int(year_diff), 
                    int(bounce_0_3), 
                    int(bounces_0_6),
                    int(mother_0_3),
                    int(mother_4_6),
                    int(mother_7_12),
                    int(mother_13_24),
                    int(mother_25_60),
                    int(mother_0_6),
                    int(mother_0_9),
                    int(mother_0_12),
                    int(mother_0_24),
                    int(mother_0_60)
                )
            
                if result == "Eligible for Loan":
                    accepted_banks.append(bank)
                else:
                    rejected_banks[bank] = result  # Store rejection reason
           
            # Usage


          
            # Streamlit UI
            st.title("Loan Eligibility Results")

            # Accepted Banks Section
            st.subheader("✅ Accepted Banks")
            if accepted_banks:
                st.markdown(" - " + "\n - ".join(accepted_banks))
            else:
                st.markdown("_No banks accepted._")

            # Rejected Banks Section
            st.subheader("❌ Rejected Banks")
            if rejected_banks:
                for bank, reason in rejected_banks.items():
                    st.markdown(f"**{bank}**: <span style='color:red; font-weight:bold;'>{reason}</span>", unsafe_allow_html=True)
                st.success("✅ Mother Loan Found")
                st.write("**Account Number:**", mother_loan["accountNumber"])
                st.write("**Bank:**", mother_loan.get("memberShortName", "Unknown"))
                st.write("**Loan Opened On:**", mother_loan.get("dateOpened", "N/A"))
                st.markdown("""
                **Bounce Summary:**
                • Last 0–3 months: {} DPDs  
                • Last 4–6 months: {} DPDs  
                • Last 7–12 months: {} DPDs  
                • Last 13–24 months: {} DPDs  
                • Last 25–60 months: {} DPDs  
                • Last 0–6 months: {} DPDs  
                • Last 0–9 months: {} DPDs  
                • Last 0–12 months: {} DPDs  
                • Last 0–24 months: {} DPDs  
                • Last 0–60 months: {} DPDs  
                """.format(
                    bounces["0_3"],
                    bounces["4_6"],
                    bounces["7_12"],
                    bounces["13_24"],
                    bounces["25_60"],
                    bounces["0_6"],
                    bounces["0_9"],
                    bounces["0_12"],
                    bounces["0_24"],
                    bounces["0_60"]
                ))  
            else:
                st.markdown("_No banks rejected._")

            
 



        except Exception as e:
            st.error(f"❌ Error: {e}")
