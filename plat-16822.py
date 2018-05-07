import json
from pprint import pprint
import copy

from util.util import getPlanIdsFromStubResponse

with open('./ref/nc-test-user-manager-staging-export.json') as f:
    staging = json.load(f)

# staging.keys()
# dict_keys(['dimensions', 'expectedResults', 'personaAccountContributions', 'personaAccountProfiles', 'personaAccountSubAccountPositions', 'personaAccountSubAccounts', 'personaAccounts', 'personaProfiles', 'personaSpouseProfiles', 'personaWorkplacePlanSubAccounts', 'personaWorkplacePlans', 'personas', 'reports', 'users'])

# staging['dimensions'].keys()
# dict_keys(['account', 'profile', 'report', 'status', 'workplacePlan'])

# add planId to dimensions
workplacePlan = staging['dimensions']['workplacePlan']
planId = {'displayName':'Plan ID'}
workplacePlan['planId'] = planId
with open('workplacePlan.json', 'w') as outfile:
    json.dump(workplacePlan, outfile)


# update persona workplace plan subaccount
personaWorkplacePlanSubAccounts = staging['personaWorkplacePlanSubAccounts']
# personaWorkplacePlanSubAccounts['1']
# {'allowsAutoEscalation': 'false',
#  'id': '1',
#  'isEligibleForManagedAccounts': 'false',
#  'isEligibleForNewContributions': 'true',
#  'source': 'employer',
#  'taxTreatment': 'pre_tax'}
# id starts from 3 to 5
for (index, taxTreatment) in enumerate(['pre-tax', 'roth', 'post-tax']):
    id = str(index + 3)
    print(id, taxTreatment)
    append_workplacePlanSubAccount =  {'allowsAutoEscalation': 'true',
        'id': id,
        'isEligibleForManagedAccounts': 'true',
        'isEligibleForNewContributions': 'true',
        'source': 'employee',
        'taxTreatment': taxTreatment}
    personaWorkplacePlanSubAccounts[id] = append_workplacePlanSubAccount

with open('personaWorkplacePlanSubAccounts.json', 'w') as outfile:
    json.dump(personaWorkplacePlanSubAccounts, outfile)

# update psersona workplace plan
personaWorkplacePlans = staging['personaWorkplacePlans']
# id starts from 2 to 13

accountType = '401k'
id = '2'
append_workplacePlan ={'accountType': accountType,
    'allowsContributionChangeImplementation': 'true',
    'autoEscalationIncrement': 'none',
    'autoEscalationSavingsEndingRate': 'none',
    'id': id,
    'managedAccountsStartDate': 'Past',
    'planSubaccounts': { "3": True, "4": True, "5": True },
    'planId': 'john_hancock_401k_plan'
    }
personaWorkplacePlans[id] = append_workplacePlan

accountType = '401a_money_purchase'
id = '3'
append_workplacePlan ={'accountType': accountType,
    'allowsContributionChangeImplementation': 'true',
    'autoEscalationIncrement': 'none',
    'autoEscalationSavingsEndingRate': 'none',
    'id': id,
    'managedAccountsStartDate': 'Past',
    'planSubaccounts': { "3": True, "5": True },
    'planId': 'john_hancock_401a_money_purchase_plan'
    }
personaWorkplacePlans[id] = append_workplacePlan

accountType = '457b'
id = '4'
append_workplacePlan ={'accountType': accountType,
    'allowsContributionChangeImplementation': 'true',
    'autoEscalationIncrement': 'none',
    'autoEscalationSavingsEndingRate': 'none',
    'id': id,
    'managedAccountsStartDate': 'Past',
    'planSubaccounts': { "3": True, "4": True },
    'planId': 'john_hancock_457b_plan'
    }
personaWorkplacePlans[id] = append_workplacePlan

accountType = '457b_government'
id = '5'
append_workplacePlan ={'accountType': accountType,
    'allowsContributionChangeImplementation': 'true',
    'autoEscalationIncrement': 'none',
    'autoEscalationSavingsEndingRate': 'none',
    'id': id,
    'managedAccountsStartDate': 'Past',
    'planSubaccounts': { "3": True, "4": True },
    'planId': 'john_hancock_457b_government_plan'
    }
personaWorkplacePlans[id] = append_workplacePlan

accountType = '457b_non_profit'
id = '6'
append_workplacePlan ={'accountType': accountType,
    'allowsContributionChangeImplementation': 'true',
    'autoEscalationIncrement': 'none',
    'autoEscalationSavingsEndingRate': 'none',
    'id': id,
    'managedAccountsStartDate': 'Past',
    'planSubaccounts': { "3": True, "4": True },
    'planId': 'john_hancock_457b_non_profit_plan'
    }
personaWorkplacePlans[id] = append_workplacePlan

accountType = 'defined_benefit'
id = '7'
append_workplacePlan ={'accountType': accountType,
    'allowsContributionChangeImplementation': 'true',
    'autoEscalationIncrement': 'none',
    'autoEscalationSavingsEndingRate': 'none',
    'id': id,
    'managedAccountsStartDate': 'Past',
    'planSubaccounts': { "3": True },
    'planId': 'john_hancock_defined_benefit_plan'
    }
personaWorkplacePlans[id] = append_workplacePlan

accountType = '457f'
id = '8'
append_workplacePlan ={'accountType': accountType,
    'allowsContributionChangeImplementation': 'true',
    'autoEscalationIncrement': 'none',
    'autoEscalationSavingsEndingRate': 'none',
    'id': id,
    'managedAccountsStartDate': 'Past',
    'planSubaccounts': { "3": True },
    'planId': 'john_hancock_457f_plan'
    }
personaWorkplacePlans[id] = append_workplacePlan

accountType = 'esop'
id = '9'
append_workplacePlan ={'accountType': accountType,
    'allowsContributionChangeImplementation': 'true',
    'autoEscalationIncrement': 'none',
    'autoEscalationSavingsEndingRate': 'none',
    'id': id,
    'managedAccountsStartDate': 'Past',
    'planSubaccounts': { "3": True },
    'planId': 'john_hancock_esop_plan'
    }
personaWorkplacePlans[id] = append_workplacePlan

accountType = 'non_qualified_defined_contribution'
id = '10'
append_workplacePlan ={'accountType': accountType,
    'allowsContributionChangeImplementation': 'true',
    'autoEscalationIncrement': 'none',
    'autoEscalationSavingsEndingRate': 'none',
    'id': id,
    'managedAccountsStartDate': 'Past',
    'planSubaccounts': { "3": True, "5": True },
    'planId': 'john_hancock_non_qualified_defined_contribution_plan'
    }
personaWorkplacePlans[id] = append_workplacePlan

accountType = 'profit_sharing'
id = '11'
append_workplacePlan ={'accountType': accountType,
    'allowsContributionChangeImplementation': 'true',
    'autoEscalationIncrement': 'none',
    'autoEscalationSavingsEndingRate': 'none',
    'id': id,
    'managedAccountsStartDate': 'Past',
    'planSubaccounts': { "3": True, "5": True },
    'planId': 'john_hancock_profit_sharing_plan'
    }
personaWorkplacePlans[id] = append_workplacePlan

accountType = 'target_benefit'
id = '12'
append_workplacePlan ={'accountType': accountType,
    'allowsContributionChangeImplementation': 'true',
    'autoEscalationIncrement': 'none',
    'autoEscalationSavingsEndingRate': 'none',
    'id': id,
    'managedAccountsStartDate': 'Past',
    'planSubaccounts': { "3": True },
    'planId': 'john_hancock_target_benefit_plan'
    }
personaWorkplacePlans[id] = append_workplacePlan

accountType = 'thrift_savings_plan'
id = '13'
append_workplacePlan ={'accountType': accountType,
    'allowsContributionChangeImplementation': 'true',
    'autoEscalationIncrement': 'none',
    'autoEscalationSavingsEndingRate': 'none',
    'id': id,
    'managedAccountsStartDate': 'Past',
    'planSubaccounts': { "3": True },
    'planId': 'john_hancock_thrift_savings_plan_plan'
    }
personaWorkplacePlans[id] = append_workplacePlan

with open('personaWorkplacePlans.json', 'w') as outfile:
    json.dump(personaWorkplacePlans, outfile)

# update account dimensions
account = staging['dimensions']['account']
account["workplacePlans"] = {'displayName':'Workplace Plans'}
with open('account.json', 'w') as outfile:
    json.dump(account, outfile)

# get personas
personas = staging['personas']

# get mapping from persona to presonaAccounts
# get stub response xml content from 909 to 1022 and store to somewhere
'''
persona_map_workplacePlanId = {}
for id in range(909, 1023):
    pid = str(id)
    planIds = getPlanIdsFromStubResponse(pid)
    persona_map_workplacePlanId[pid] = planIds

with open('persona_map_workplacePlanId.json', 'w') as outfile:
    json.dump(persona_map_workplacePlanId, outfile)

'''

with open('persona_map_workplacePlanId.json', 'r') as infile:
    persona_map_workplacePlanId = json.load(infile)

personaAccounts_map_planIds_with_personas = {}
for i in range(909, 1022):
    personaId = str(i)
    personaAccounts_ids = personas[personaId]['accounts'].keys()
    personaPlanIds = persona_map_workplacePlanId[personaId]

    # id is account id
    for index, id in enumerate(personaAccounts_ids):
        if id not in personaAccounts_map_planIds_with_personas:
            personaAccounts_map_planIds_with_personas[id]= {}
        planId = personaPlanIds[index] if index < len(personaPlanIds) else 'null'
        if planId not in personaAccounts_map_planIds_with_personas[id]:
            personaAccounts_map_planIds_with_personas[id][planId] = []
        personaAccounts_map_planIds_with_personas[id][planId].append(personaId)

# planId map plan ID
personaWorkplacePlans_planId_map_id = {}
for id in range(2,14):
    index = str(id)
    personaWorkplacePlans_planId_map_id[personaWorkplacePlans[index]['planId']] = index

# build new personaAccounts with mapping to wokrplacePlan
# based on stub response
# starts from (old_id + 1000)
personaAccounts = staging['personaAccounts']

for account_id in personaAccounts_map_planIds_with_personas:
    new_personaAccount = copy.deepcopy(personaAccounts[account_id])
    new_personaAccount['id'] = str(int(new_personaAccount['id']) + 1000)
    # print(personaAccounts_map_planIds_with_personas[account_id])
    # print(personaAccounts[account_id])
    for planId in personaAccounts_map_planIds_with_personas[account_id].keys():
        if planId not in personaWorkplacePlans_planId_map_id:
            print('*' * 20, planId)
            continue
        plan_id = personaWorkplacePlans_planId_map_id[planId]
        new_personaAccount['workplacePlans'] = {plan_id: True}
        break
    # print(new_personaAccount)
    personaAccounts[new_personaAccount['id']] = new_personaAccount


with open('personaAccounts.json', 'w') as outfile:
    json.dump(personaAccounts, outfile)


for i in range(909, 1022):
    id = str(i)
    accounts = {}
    for account in personas[id]['accounts']:
        accounts[str(1000 + int(account) % 1000)] = True
    personas[id]['accounts'] = accounts

with open('personas.json', 'w') as outfile:
    json.dump(personas, outfile)
