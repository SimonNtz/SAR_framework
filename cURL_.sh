curl -H Content-Type: application/json -X POST http://0.0.0.0:81/SLA_CLI -d
 '{"SLA":
    {"requirements": [1000, 1],
    "product_list": ["S1A_IW_GRDH_1SDV_20151226T182813_20151226T182838_009217_00D48F_5D5F",
                    "S1A_IW_GRDH_1SDV_20160424T182813_20160424T182838_010967_010769_AA98"]},
   "result": {}}'
