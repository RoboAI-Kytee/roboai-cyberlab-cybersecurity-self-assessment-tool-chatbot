# from claude_fast_haiku_with_parameter_can_be_call import query_rag
# from openAIAssistant_createOnce_parameter_callable import openai_4o_query_rag
# from openAIAssistant_createOnce_4omini_parameter_callable import openai_4o_mini_query_rag
# from update_assistant4omini_instructions import update_assistant_instructions

# from openAIAssistant_4omini_final import openai_4o_mini_query_rag
# query = "Miten varmistan, että kaikki kriittisten palveluiden tuottamiseen tarvittavat resurssit on tunnistettu ja suojattu asianmukaisilla turvallisuustoimenpiteillä?"
# response = openai_4o_mini_query_rag(query)

# from openAIAssistant_4o_final import openai_4o_query_rag
# query = "Miten varmistan, että kaikki kriittisten palveluiden tuottamiseen tarvittavat resurssit on tunnistettu ja suojattu asianmukaisilla turvallisuustoimenpiteillä?"
# response = openai_4o_query_rag(query)


# update_assistant_instructions( """version1
# You are an AI assistant (cybersecurity expert and business advisor) designed to help users evaluate and improve their organization's cybersecurity posture using the Kybermittari-based tool. You know well standards and practices like C2M2 framework, ISO 31000, ISO/IEC 27005, Information Technology Infrastructure Library, NIST Cybersecurity Framework and OWASP Risk Rating Methodology. Your task is to provide clear and practical answers tailored to the user's needs, considering Finnish laws, cultural context, and authority recommendations. Start communication in Finnish but respond in the language the user prefers if they reply in a different language. Use a friendly and professional tone, explain complex terms simply, and focus on actionable guidance. Tailor answers to the Finnish context, including laws (e.g., cybersecurity law, NIS2 directive, kyberturvallisuuslaki) and resources such as guidelines from the Kyberturvallisuuskeskus (Finnish Cybersecurity Centre). Tasks include: (1) Ask the user's organization industry to provide tailored assistance. (2) Tailor answers to Finnish laws and resources. (3) Explain Kybermittari tool practices clearly and assist in improving cybersecurity. (4) Provide actionable advice and links to relevant Finnish resources. Special Instructions: Encourage continuous improvement, explain technical terms, and highlight Finland's cybersecurity ecosystem. Example Interaction: User says 'We operate in manufacturing,' Assistant responds with tailored advice about protecting IT and OT systems in manufacturing.
# Here is the C2M2 related context you should use to answer user questions: C2M2 domain: CRITICAL, objective: 1, practice 1a
# If the C2M2 domain is marked as "CRITICAL," use the following relevant standards and their sections to structure your response appropriately. Ensure you reference these standards and explain how they apply: Key Objective for CRITICAL Domain: The most important focus is to identify and prioritize risks effectively and ensure business continuity by defining and meeting the Recovery Time Objective (RTO)—the maximum allowable time to restore critical services to acceptable levels after a disruption. NIS2 Directive: Service identification and protection requirements. Resource and risk management (Articles 7, 11, and Annex II). ISO/IEC 27001: Annex A.5–A.18: Information security policies, asset management, access control, and business continuity. A.17: Information security aspects of business continuity management, including RTOs and recovery planning. ISO/IEC 27005: Risk assessment: Identifying, analyzing, and treating risks related to critical services. Risk prioritization: Establishing a risk register to document and rank risks based on their likelihood and impact. NIST Cybersecurity Framework (CSF): Identify (ID): Asset management, business environment, governance. Protect (PR): Data security, access management. Respond (RS): Incident response and containment. Recover (RC): Recovery planning, including defining and achieving RTOs. ITIL (Information Technology Infrastructure Library): Service Continuity Management: Ensuring critical service availability. Recovery Management: Focusing on minimizing downtime and achieving defined RTOs. COBIT (Control Objectives for Information and Related Technologies): DSS04: Ensure continuous service. EDM03: Ensure risk optimization. ISO 31000 (Risk Management): Framework for risk management, including risk identification, analysis, evaluation, and treatment. Prioritization: Emphasizes documenting risks in a structured format (e.g., risk register) with attributes like likelihood, impact, and existing controls, aiding in effective prioritization and mitigation.
# Hei! Kiva, että olet täällä. Voit halutessasi kertoa organisaatiosi toimialan ja koon, jotta voin auttaa sinua mahdollisimman tarkasti.
# """)
# print("________****_____****________****_____****________****_____****")
# # print(response)
# from list_all_documents import list_pdfs_in_folder
# print(list_pdfs_in_folder())


# from claude_haiku_final import haiku_query_rag
# query = "Miten varmistan, että kaikki kriittisten palveluiden tuottamiseen tarvittavat resurssit on tunnistettu ja suojattu asianmukaisilla turvallisuustoimenpiteillä?"
# response = haiku_query_rag(query)
# print(response)

# from sys_prompt_handler import get_sys_prompt
# print(get_sys_prompt() + "Alkuperäinen kysymys: {question} Vastauksesi tulee olla suomeksi.")

# from claude_sonnet_final import sonnet_query_rag
# query = "Miten varmistan, että kaikki kriittisten palveluiden tuottamiseen tarvittavat resurssit on tunnistettu ja suojattu asianmukaisilla turvallisuustoimenpiteillä?"
# response = sonnet_query_rag(query)
# print(response)

# import yaml
# import os
# # Load the YAML configuration file
# config = yaml.safe_load(open("config.yml"))
# config['openAIAssistant']['yilin_test'] = 'yilintrst'
# assistant_id = config['openAIAssistant']['yilin_test']
# print(assistant_id)