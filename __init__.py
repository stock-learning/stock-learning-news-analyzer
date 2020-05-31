
import boto3
import csv
import json

# Comprehend constant
region = 'us-east-2'
aws_access_key_id = 'AKIAJJB2PO54FEPYHUZQ'
aws_secret_access_key = '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'

if __name__ == '__main__':
    _text = 'Amazon Comprehend is a natural language processing (NLP) service that uses machine learning to find insights and relationships in text.'
    _comprehend = boto3.client('comprehend', region_name=region, aws_secret_access_key=aws_secret_access_key, aws_access_key_id=aws_access_key_id)
    _language_code = _comprehend.detect_dominant_language(Text=_text)['Languages'][0]['LanguageCode']
    print(_comprehend.detect_entities(Text=_text, LanguageCode=_language_code)) # detecting named entities
    print(_comprehend.detect_key_phrases(Text=_text, LanguageCode=_language_code)) # detecting key phrases
    print(_comprehend.detect_sentiment(Text=_text, LanguageCode=_language_code)) # detecting sentiment