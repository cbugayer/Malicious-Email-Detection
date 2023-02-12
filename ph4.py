from LexicalUrlFeatures import LexicalURLFeatures
from ContentFeatures import ContentFeatures
from HostFeatures import HostFeatures
import whois
import pandas as pd
data0 = pd.read_csv("online-valid.csv")
phishurl = data0.sample(n = 20, random_state = 12).copy()
phishurl = phishurl.reset_index(drop=True)
data1 = pd.read_csv("Benign_list_big_final.csv")
data1.columns = ['URLs']
#Collecting 1,000 Legitimate URLs randomly
legiurl = data1.sample(n = 20, random_state = 12).copy()
legiurl = legiurl.reset_index(drop=True)
feat_names = ['UrlLength','PathLength','Hostlength','HostIsIp','PortInUrl','NumDigits','NumQueryParams',
            'NumFragments','IsEncoded','NumEncodings','NumSubDirs','NumPeriods','HasClient','HasAdmin',
            'HasServer','HasLogin','HasAtsign','Redirection','UrlShortened','UsesHttps','DashInDomain',
            'HtmlLen','NumHtmlTags','NumHiddenTags','NumScriptTags','NumIframes','NumEmbeds','NumHyperLinks',
            'NumEvalFuncs','WebForwards', 'DomainAge', 'DomainIntendedLife_Span','LifeRemaining',
            'IsLive','ConnectionSpeed','AvgUpdateFrequency','NumUpdates','TTL', "ClassLabel"]
def feat_extraction(url, label):
    UrlFeats = LexicalURLFeatures(url)
    ContFeats = ContentFeatures(url)
    HostFeats = HostFeatures(url)

    feats = []
    ph_methods = ['url_length','url_path_length','url_host_length','url_host_is_ip','url_contains_port','num_of_digits',
                'num_of_parameters','num_of_fragments','is_encoded','num_encoded_chars','num_of_subdirectories',
                'num_of_periods','has_client_in_string','has_admin_in_string','has_server_in_string',
                'has_login_in_string','has_at_sign','redirection','tiny_url','uses_https','dash_in_domain']
    ph2_methods = ['length_of_html','number_of_html_tags','number_of_hidden_tags','number_of_script_tags','number_iframes',
                'number_embeds','number_of_hyperlinks','number_of_eval_functions','forwarding']
    ph3_methods = ['url_age','url_intended_life_span','url_life_remaining','url_is_live','url_connection_speed',
                'average_update_frequency','number_of_updates','ttl_from_registration']
    for method in ph_methods:
        feats.append(getattr(UrlFeats, method)())  # call
    for method in ph2_methods:
        feats.append(getattr(ContFeats, method)())  # call
    for method in ph3_methods:
        feats.append(getattr(HostFeats, method)())  # call
    feats.append(label)

#Extracting the feautres & storing them in a list
legi_features = []
label = 0

for i in range(0, legiurl.shape[0]):
  url = legiurl['URLs'][i]
  legi_features.append(feat_extraction(url,label))
