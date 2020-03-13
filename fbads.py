import sys
from flask import Flask
from flask import render_template, request
app = Flask(__name__)
sys.path.append('~/.virtualenvs/fbads/lib/python3.6/site-packages') # Replace this with the place you installed facebookbusiness using pip
sys.path.append('~/.virtualenvs/fbads/lib/python3.6/site-packages/facebook_business-3.0.0-py2.7.egg-info') # same as above

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.targeting import Targeting
from facebook_business.adobjects.adsinsights import AdsInsights

@app.route("/")
def get(name=None):
	return render_template("index.html", name=name)

#my_app_id = '176563503656887'
#my_app_secret = '2deafbb852358b22d10a09e78b99fae8'

#ad accounts and access token(testing)
@app.route("/data", methods=['POST'])
def data():

	my_access_token = request.form['acctoken']
	FacebookAdsApi.init(access_token=my_access_token)
	adacc = 'act_' + request.form['accid']
	my_account = AdAccount(adacc)

	#getting all fields and removing some fields that are not in the document that produce errors
	Fields_Campaign = [attr for attr in dir(Campaign.Field) if not callable(getattr(Campaign.Field, attr)) and not attr.startswith("__")]
	Fields_Ad =[attr for attr in dir(Ad.Field) if not callable(getattr(Ad.Field, attr)) and not attr.startswith("__")]
	Fields_AdCreative = [attr for attr in dir(AdCreative.Field) if not callable(getattr(AdCreative.Field, attr)) and not attr.startswith("__")]
	a = ['call_to_action', 'image_file', 'is_dco_internal']
	Fields_AdCreative = [i for i in Fields_AdCreative if i not in a]
	Fields_AdSets = [attr for attr in dir(AdSet.Field) if not callable(getattr(AdSet.Field, attr)) and not attr.startswith("__")]
	b = ['line_number', 'rb_prediction_id', 'time_start', 'time_stop', 'topline_id', 'tune_for_category','upstream_events', 'full_funnel_exploration_mode', 'daily_imps', 'date_format', 'execution_options', 'campaign_spec']
	Fields_AdSets = [i for i in Fields_AdSets if i not in b]
	Fields_AdsInsights = [attr for attr in dir(AdsInsights.Field) if not callable(getattr(AdsInsights.Field, attr)) and not attr.startswith("__")]
	c = ['dwell_3_sec', 'dwell_5_sec', 'actions_per_impression', 'actions_results', 'activity_recency', 'ad_format_asset', 'age', 'amount_in_catalog_currency', 'app_store_clicks', 'attention_events_per_impression', 'attention_events_unq_per_reach', 'body_asset', 'call_to_action_asset', 'call_to_action_clicks', 'campaign_delivery', 'campaign_end', 'campaign_start', 'cancel_subscription_actions', 'card_views', 'catalog_segment_actions', 'catalog_segment_value_in_catalog_currency', 'catalog_segment_value_mobile_purchase_roas', 'catalog_segment_value_website_purchase_roas', 'conditional_time_spent_ms_over_10s_actions', 'conditional_time_spent_ms_over_15s_actions', 'conditional_time_spent_ms_over_2s_actions', 'conditional_time_spent_ms_over_3s_actions', 'conditional_time_spent_ms_over_6s_actions', 'contact_actions', 'contact_value', 'cost_per_action_result', 'cost_per_completed_video_view', 'cost_per_contact', 'cost_per_customize_product', 'cost_per_donate', 'cost_per_dwell', 'cost_per_dwell_3_sec', 'cost_per_dwell_5_sec', 'cost_per_dwell_7_sec', 'cost_per_find_location', 'cost_per_schedule', 'cost_per_start_trial', 'cost_per_submit_application', 'cost_per_subscribe', 'cost_per_total_action', 'country', 'creative_fingerprint', 'customize_product_actions', 'customize_product_value', 'deduping_1st_source_ratio', 'deduping_2nd_source_ratio', 'deduping_3rd_source_ratio', 'deduping_ratio', 'deeplink_clicks', 'description_asset', 'device_platform', 'dma', 'donate_actions', 'donate_value', 'dwell_3_sec, dwell_5_sec', 'dwell_7_sec', 'dwell_rate', 'earned_impression', 'find_location_actions', 'find_location_value', 'frequency_value', 'gender', 'hourly_stats_aggregated_by_advertiser_time_zone', 'hourly_stats_aggregated_by_audience_time_zone', 'image_asset', 'impression_device', 'impressions_auto_refresh', 'impressions_gross', 'link_url_asset', 'media_asset', 'newsfeed_avg_position', 'newsfeed_clicks', 'newsfeed_impressions', 'optimization_goal', 'performance_indicator', 'place_page_id', 'placement', 'platform_position', 'product_id', 'publisher_platform', 'recurring_subscription_payment_actions', 'region', 'rule_asset', 'schedule_actions', 'schedule_value', 'start_trial_actions', 'start_trial_value', 'submit_application_actions', 'submit_application_value', 'subscribe_actions', 'subscribe_value', 'thumb_stops', 'title_asset', 'today_spend', 'total_action_value', 'total_actions', 'total_unique_actions', 'unique_impressions', 'video_asset', 'video_complete_watched_actions', 'video_completed_view_or_15s_passed_actions', 'website_clicks']
	Fields_AdsInsights = [i for i in Fields_AdsInsights if i not in c]


	#get data from campaigns to ads insights
	alldata = []
	campaign = my_account.get_campaigns(fields=Fields_Campaign)
#	ad_Creative = my_account.get_ad_creatives(fields =Fields_AdCreative)
#	ads = my_account.get_ads(fields=Fields_Ad)
#	ad_sets =  my_account.get_ad_sets(fields=Fields_AdSets)
#	ad_insight = my_account.get_insights(fields = Fields_AdsInsights)


	alldata.append(campaign)
#	alldata.push(ad_Creative)
#	alldata.append(ads)
#	alldata.push(ad_sets)
#	alldata.append(ad_insight)

	return render_template("data.html", data=alldata)


if __name__ == '__main__':
	app.run(port='8000', debug=True)
