# Defining raw data sources

BASE_PATH = "/Volumes/bike_lakehouse/bronze/raw_sources/source"

CRM = "crm"
ERP = "erp"

INGESTION_CONFIG = [
    {
        "source": CRM,
        "path": f"{BASE_PATH}_{CRM}/cust_info.csv",
        "table": f"{CRM}_cust_info",
    },
    {
        "source": CRM,
        "path": f"{BASE_PATH}_{CRM}/prd_info.csv",
        "table": f"{CRM}_prd_info",
    },
    {
        "source": CRM,
        "path": f"{BASE_PATH}_{CRM}/sales_details.csv",
        "table": f"{CRM}_sales_details",
    },
    {
        "source": ERP,
        "path": f"{BASE_PATH}_{ERP}/CUST_AZ12.csv",
        "table": f"{ERP}_CUST_AZ12",
    },
    {
        "source": ERP,
        "path": f"{BASE_PATH}_{ERP}/LOC_A101.csv",
        "table": f"{ERP}_LOC_A101",
    },
    {
        "source": ERP,
        "path": f"{BASE_PATH}_{ERP}/PX_CAT_G1V2.csv",
        "table": f"{ERP}_PX_CAT_G1V2",
    },
]