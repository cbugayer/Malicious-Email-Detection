# Malicious-Email-Detection
Data Privacy Project with Charles Bugayer, Erick Mungai, Vernon Otieno, and Kelvin Forson

## Reason for study
A new study by Cofense found that one in ten emails were classified as malicious with more than 50% of those linked to fraudulent attempts to gather a user's login and system information, known as credential phishing. With email being a primary form of communication, users are at a high risk of falling victim to phishing attacks. In cases where phishing attacks are successful, users might end up unknowingly giving up their personal information or credit card information which might be used by fraudsters in committing fraud which results in an individual’s financial loss. 

Additionally, phishing is not only detrimental to individuals. Corporations, such as healthcare institutions, that hold sensitive information about their users could also suffer data breaches from phishing attacks resulting in the leaking of user’s confidential information. 

Moreover, the modern computerized society has forced older people to adapt to current technology trends. This rapid exposure presents a huge challenge due to inadequate training in the usage of technology. Since they might not be familiar with the ways in which they can protect their information, they greatly stand the risk of phishing attacks, which could lead to their personal information being compromised. We aim to develop a tool that minimizes the odds of encountering phishing attacks by providing a succinct report of the threat levels of new email messages. 

## Datasets Description
Phishing Dataset for Machine Learning | Kaggle - This dataset contains 48 features extracted from 5000 phishing webpages and 5000 legitimate webpages, which were downloaded from January to May 2015 and from May to June 2017. It will be useful in building a machine learning model that identifies phishing emails.

## Methodology
We will create a link checker that finds links in an email. Thereafter, we will create a machine learning model, trained and tested on our dataset, that determines the chances of a linked webpage being a phishing attack. We will utilize a natural language parser that scans the content of the email message and retrieves different suspicious texts, symbols, etc. Finally, we will create a browser extension that uses our model.

## Pre-work
Due to the nature of our project, we plan to leverage different libraries in python for computing statistics about the data set such as panda, matplotlib, etc. Also, we plan to familiarize ourselves with the technology stack involved in building a Google Chrome Extension in order to expose our tool to a wide group of people.

## Actionable Items
We plan on meeting twice a week to work on the project (Tuesdays and Thursdays - 6-7:30pm).

## Milestones & Timelines
Data Extraction and Cleaning -  1/28
Design of Machine Learning Model - 2/6
Training and Testing - 2/10
Iteration of Machine Learning Model - 2/20
Chrome Extension Tool - 3/10
Deployment of Tool - 3/13

## Backup Plan
In case we are not able to build the Chrome Extension, we will create a simple web page where users will copy and paste the email in doubt, and the analysis of the email will then display on the same web page.

## Allocation of tasks
Due to the nature of our project, we plan to work on the different tasks together. Should the need to divide tasks arise, we will do so accordingly. Everyone will be tasked with keeping the group accountable and on schedule.

## References
https://www.frontiersin.org/articles/10.3389/fcomp.2021.563060     

Is This Phishing? Older Age Is Associated With Greater Difficulty Discriminating Between Safe and Malicious Emails - PMC (nih.gov)

Phishing suspiciousness in older and younger adults: The role of executive functioning - PMC (nih.gov)

New Study on Malicious Emails - Northwestern University 

https://www.infosecurity-magazine.com/news/one-10-reported-emails-malicious/

## Research Paper
https://arxiv.org/pdf/2201.10752.pdf 
