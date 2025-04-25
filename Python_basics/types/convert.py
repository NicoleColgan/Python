import ast
import csv
import pandas as pd
import json
# context="['Advisory: HPE ProLiant, Apollo and Synergy Gen10 Platforms - Systems Supporting Intel Xeon Scalable Processors May Experience Uncorrectable Machine Check Exception (UMCE) Errors Advisory: HPE ProLiant, Apollo and Synergy Gen10 Platforms - Systems Supporting Intel Xeon Scalable Processors May Experience Uncorrectable Machine Check Exception (UMCE) Errors Document Subtype: Customer AdvisorySeverity: HighDocument ID: a00110879en_usLast Updated: 2021-02-10Document Version: 1 DESCRIPTION Intel has released new specification updates to their Xeon Scalable Processors (Skylake) and Second Generation Xeon Scalable Processors (Cascade Lake) in January 2021 that detail two new errata which are resolved, except for the HPE ProLiant e910/e910t Server Blade, by applying the System ROM version 2.42. For reference, the specification update may be downloaded from here for the Second Generation Scalable Processors and from here for the First Generation Scalable Processors. The failure symptoms of these two errata are described below: Failure Symptom 1 This failure only affects the Xeon Second Generation Scalable Processors. A failure will be logged in the Integrated Management Log (IML) similar to the following: Uncorrectable Machine Check Exception (Processor 2, APIC ID 0x00000070, Bank 0x00000003, Status 0xBE000000\'00800400, Address 0x00000000\'06EF5128, Misc 0x00000000\'06EF5128). ACTION: Update the system firmware. If the issue persists, contact support. The following conditions are necessary to be considered a match for this issue: The Bank value must have a value of 0x00000003 The lower 8 characters of the Status field must exactly match the value \'00800400\' (see bold characters in Status field above). This will be the only error logged for the failure in most instances. However, it is possible for one additional UMCE to be logged for Bank 0x00000004 with a Status field identical to the Status field of the Bank 3 error. This failure is defined as Errata CLX53 in the Intel Xeon Second Generation Scalable Processor specification update. Failure Symptom 2 This failure affects both Xeon Scalable Processors and Xeon Second Generation Scalable Processors. One or more failures will be logged in the Integrated Management Log similar to the following for a failure event: Uncorrectable Machine Check Exception (Processor 2, APIC ID 0x00000070, Bank 0x00000009, Status 0xFE200000\'000C110A, Address0x00000000\'06EF5128, Misc 0x00A44126\'005A4086). ACTION: Update the system firmware. If the issue persists, contact support. The following conditions are necessary to be considered a match for this issue: The Bank must be either 0x00000009, 0x0000000A, or 0x0000000B. The lower 8 characters of the Status field must exactly match the value \'000C110A\' (see bold characters in Status field above). In addition, posted interrupts must be enabled in the operating system. Posted interrupts are often used in virtualized environments to increase performance. This failure is defined as errata CLX52 in the Xeon Second Generation Scalable Processors specification update and as SKX123 in the Xeon Scalable Processors specification update.']"

     
df = pd.read_csv('20250312-094122.csv')
data=[]
df["reference_contexts"] = df["reference_contexts"].apply(ast.literal_eval)
   
    # Iterate over each row in the CSV file
for query, reference, reference_contexts in zip(df.user_input, df.reference, df.reference_contexts):
    data.append({
        "query": query,
        "reference": reference,
        "reference_context": reference_contexts
    })

print(f"data={data}")
df=pd.DataFrame(data)
df["reference_context"] = df["reference_context"].apply(json.dumps)
df.to_csv("output.csv", index=False)

# context = '["item1", "item2"]'  
# print(f"type={type(context)}")
# print(f"type after={type(ast.literal_eval(context))}")