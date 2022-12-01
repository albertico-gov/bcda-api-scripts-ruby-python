#!/usr/bin/env ruby

require 'http'
require 'json'

# BCDA API sandbox endpoints
BCDA_API_TOKEN_ENDPOINT = "https://sandbox.bcda.cms.gov/auth/token"
BCDA_API_EXPORT_ENDPOINT = "https://sandbox.bcda.cms.gov/api/v2/Patient/$export"

# BCDA API headers
BCDA_API_TOKEN_HEADERS = { accept: "application/json", prefer: "respond-async" }
BCDA_API_EXPORT_HEADERS = { accept: "application/fhir+json", prefer: "respond-async" }
BCDA_API_STATUS_HEADERS = { accept: "application/fhir+json", prefer: "respond-async" }

# Credentials
# Visit the following link for testing credentials: https://bcda.cms.gov/guide.html#try-the-api
CLIENT_ID = "REPLACE-WITH-SANDBOX-CLIENT-ID"
CLIENT_SECRET = "REPLACE-WITH-SANDBOX-CLIENT-SECRET"

puts "Creating access token..."
response = HTTP.headers(BCDA_API_TOKEN_HEADERS).basic_auth(user: CLIENT_ID, pass: CLIENT_SECRET).post(BCDA_API_TOKEN_ENDPOINT)

if response.code != 200
  puts "Error: #{response.code} - #{response.body}"
  exit 1
end

puts "Access token retrieved!"
access_token = JSON.parse(response.body)["access_token"]

puts "Requesting data export..."
response = HTTP.headers(BCDA_API_EXPORT_HEADERS).auth("Bearer #{access_token}").get(BCDA_API_EXPORT_ENDPOINT)

if response.code != 202
  puts "Error: #{response.code} - #{response.body}"
  exit 1
end

puts "Data export successfully enqued!"
job_url = response.headers["Content-Location"]
puts "Job URL: #{job_url}"

puts "Checking job status..."
loop do
  response = HTTP.headers(BCDA_API_STATUS_HEADERS).auth("Bearer #{access_token}").get(job_url)

  if response.code == 200
    job_completion_date = response.headers["Date"]
    job_expiration_date = response.headers["Expires"]
    puts "Job FINISHED on #{job_completion_date}"
    puts "Job EXPIRES on #{job_expiration_date}"
    puts JSON.pretty_generate(JSON.parse(response.body))
    break
  elsif response.code == 202
    job_progress = response.headers["X-Progress"]
    puts "Job still being processed: #{job_progress}"
    sleep 5
  else
    puts "Unexpected error!"
    puts response.code
    puts response.body
    break
  end
end
