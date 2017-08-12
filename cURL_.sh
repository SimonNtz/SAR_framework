curl -H "Content-Type: application/json" -X POST http://147.228.242.171:81/SLA_INIT -d
 '{"SLA":
    {"requirements": [1000, 1],
    "product_list": ["S1A_IW_GRDH_1SDV_20151226T182813_20151226T182838_009217_00D48F_5D5F",
                    "S1A_IW_GRDH_1SDV_20160424T182813_20160424T182838_010967_010769_AA98"]},
   "result": {"s3_credentials":['']}}'


curl -H "Content-Type: application/json" -X POST http://localhost/SLA_INIT -d
'{"specs_vm":{"mapper":[4,16,100], "reducer":[1,0,5,10]},
"s3_credentials":["sos.exo.io",
                  "eodata_output",
                  "EXOebcbfc157bb5422c00177a88",
                  "LKXqsT6jlXPWzSlMatfPXFcM0VE-ZaJykNlOQBQPDro"],
                  "product_list": ["S1A_IW_GRDH_1SDV_20151226T182813_20151226T182838_009217_00D48F_5D5F"]}'
