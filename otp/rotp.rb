#!/usr/bin/ruby

require 'rotp'

if ARGV.length != 1
  puts "Incorrect arguments"
  exit 1
end

code = ARGV[0]

totp = ROTP::TOTP.new(code, issuer: "Issuer")
puts totp.now

