#!/usr/bin/env python3
import csv
import requests
from model import City, Flight

BASE_URL = "http://localhost:8000"
cities = "RAI,CPT,JNB,ALG,AAE,CZL,ORN,BUG,CAB,LAD,COO,FRW,GBE,MUB,PKW,BOY,OUA,SID,BBY,BGU,BGF,BBT,IRO,BIV,CRF,ODA,AEH,MQQ,NDJ,AJN,HAH,YVA,BZV,PNR,FIH,LIQ,ASK,JIB,AUE,ABS,AAC,AAC,ALY,ATZ,ASW,HBH,CAI,EMY,HRG,UVL,LXR,MUH,UVL,PSD,SKV,SSH,SEW,SSG,ADD,LBQ,LBV,MFF,MJL,MVB,POG,UVE,BJL,ACC,ABJ,BYK,DJO,HGO,MJC,SPY,ZSS,MYD,MBA,NBO,MSU,MLW,ROB,BEN,SEB,TIP,TNR,MJN,BLZ,LLW,BKO,NDB,NKC,OUZ,DZA,AGA,AHU,CAS,CMN,FEZ,RAK,OZZ,OUD,RBA,TNG,BEW,MPM,MPA,KMP,LUD,OKU,OND,OMD,NDU,SWP,TSB,ERS,WDH,AJY,RLT,MFQ,NIM,ZND,ABV,KAN,LOS,PHC,RUN,KGL,TMS,DKR,SEZ,FNA,MGQ,AGZ,ALJ,ADY,BFN,DUR,ELS,ELL,GRJ,KIM,KLZ,HLA,LUJ,MGH,MEZ,MBM,MZF,NLP,NCS,OUH,PHW,PZB,PTG,NTY,PBZ,PLZ,PRY,RCB,SIS,SZK,SBU,TCU,ULD,UTT,UTN,VYD,WVB,WEL,KSL,KRT,PBM,MTS,ARK,DAR,JRO,DJE,MIR,SFA,TUN,EBB,ULU,FKI,FBM,CIP,KIW,LUN,MFU,NLA,BFO,BUQ,GWE,HRE,HWN,MVZ,SAY,VFA,SPK,OKD,HKG,UKB,UKY,NGO,TYO,HND,NRT,MLE,KTM,ICN,SEL,CMB,BZL,CGP,DAC,ZYL,PBH,PEK,NAY,SHA,PVG,TSN,XMN,DGM,CAN,SZX,NNG,HRB,ZJK,WUH,AMD,ATQ,QNB,IXB,BLR,BDQ,IXG,BHO,BBI,BOM,CCU,CCJ,IXC,MAA,COK,CJB,DEL,GOI,GAU,HYD,JAI,JLR,IXW,QJU,CCU,LKO,MAA,NAG,PAT,PNQ,RAJ,IXR,SXR,STV,TRV,TRZ,VNS,AXT,ASJ,AOJ,KMQ,QCB,CTS,FUK,FKS,HAC,HKD,HIJ,LSG,KOJ,KCZ,KMJ,KUH,MMJ,MYJ,MMY,HNA,KMI,NGS,KIJ,OIT,OKJ,OKA,OSA,ITM,KIX,SDS,CTS,SDJ,TAK,TKS,TOY,GAJ,YOK,CGQ,ADX,ALA,TSE,ICN,DLC,SHE,MFM,MRU,RRG,ULN,XIY,TNA,TAO,TYN,CTU,CKG,QPG,SIN,PUS,DYU,KHH,MZG,TPE,TAY,SKD,TAS,TMZ,URC,HGH,PTP,BON,CUR,SXM,NEV,SKB,UVF,SLU,SFG,SVD,HAV,HOG,SCU,VRA,LRM,POP,PUJ,SDQ,PAP,KIN,MBJ,FDF,BQN,MAZ,PSE,SJU,TAB,POS,STX,STT,EIS,VIJ,EIS,FPO,NAS,GCM,AXA,ANU,AUA,CCZ,GHB,GBI,MHH,ELH,RSD,ZSA,TCB,BGI,BDA,PTY,SJO,SAL,RTB,SAP,SDH,TGU,BZE,GUA,MGA,SJJ,SOF,NAN,SUV,SUV,BUD,SKP,BUH,OTP,EVN,BAK,MSQ,OMO,BOJ,GOZ,ROU,SLS,TGV,VAR,VID,DBV,LSZ,OSI,PUY,RJK,SPU,ZAD,ZAG,QUF,TLL,TBS,RIX,VNO,OHD,CND,AER,KHV,HTA,IKT,KZN,MRV,MOW,DME,SVO,VKO,MMK,OVB,LED,UUD,VLU,ARH,YKS,BTS,LJU,MBX,KBP,IEV,LWO,NLV,ODS,SIP,BEG,INI,QND,TGD,PRN,TIV,TIA,INN,SZG,VIE,CPH,HEL,BER,SXF,TXL,DRS,HAM,ATH,HEW,CFU,KGS,JMK,MJT,RHO,SKG,IBZ,ORK,DUB,GWY,KIR,NOC,SNN,CAG,MLA,BGO,OSL,TRF,KRK,WAW,LIS,PDL,PMI,SVQ,VLC,GOT,STO,ARN"

def main():
    # insert cities
    for city in cities.split(","):

        city = City(
            city_name=city,
            airport={
                "city_name": city,
                "airport_dest": city,
                "flights": [
                ]
        })

        r = requests.post(BASE_URL+"/flights/add_city/", json=city.model_dump())
        if not r.ok:
            print(f"Failed to post city {r} - {city}")
        else:
            print(f"Created city - {r.status_code} - {city}")

    
    # insert flights

    with open("flight_passengers.csv") as fd:
        flight_csv = csv.DictReader(fd)
        for flight in flight_csv:
            

            _from = flight['from']
            flight = Flight(
                airline=flight['airline'],
                from_location=flight['from'],
                to_location=flight['to'],
                day=int(flight['day']),
                month=flight['month'],
                year=int(flight['year']),
                age=int(flight['age']),
                gender=flight['gender'],
                reason=flight['reason'],
                stay=flight['stay'],
                transit=flight['transit'],
                connection=bool(flight['connection']),
                wait=int(flight['wait'])
            )

            # import pdb; pdb.set_trace() # check for empty fields

            x = requests.post(BASE_URL+f"/flights/{_from}", json=flight.model_dump())
            if not x.ok:
                print(f"Failed to post flight {x} - {flight}")
            else:
                print(f"Created flight - {r.status_code} - {flight}")
    

if __name__ == "__main__":
    main()