from LexicalUrlFeatures import LexicalURLFeatures
from ContentFeatures import ContentFeatures
from HostFeatures import HostFeatures

def feature_extraction(url):
    UrlFeats = LexicalURLFeatures(url)
    ContFeats = ContentFeatures(url)
    HostFeats = HostFeatures(url)

    feats = []
    ph_methods = ['url_length','url_path_length','url_host_length','url_host_is_ip','url_contains_port','num_of_digits',
                'num_of_parameters','num_of_fragments','is_encoded','num_encoded_chars','num_of_subdirectories',
                'num_of_periods','has_client_in_string','has_admin_in_string','has_server_in_string',
                'has_login_in_string','has_at_sign','redirection','tiny_url','uses_https','dash_in_domain']
    ph2_methods = ['number_of_html_tags','number_of_hidden_tags','number_of_script_tags','number_iframes',
                'number_embeds','number_of_hyperlinks','number_of_eval_functions','forwarding']
    ph3_methods = ['url_age','url_intended_life_span','url_life_remaining',
                'average_update_frequency','number_of_updates','ttl_from_registration']
    for method in ph_methods:
        feats.append(getattr(UrlFeats, method)())  # call
    for method in ph2_methods:
        feats.append(getattr(ContFeats, method)())  # call
    for method in ph3_methods:
        feats.append(getattr(HostFeats, method)())  # call
    return feats