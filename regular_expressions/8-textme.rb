#!/usr/bin/env ruby
output1 = ARGV[0].scan(/(?<=\[from\:).*?(?=\])/).join
output2 = ARGV[0].scan(/(?<=\[to\:).*?(?=\])/).join
output3 = ARGV[0].scan(/(?<=\[flags\:).*?(?=\])/).join
puts "#{output1},#{output2},#{output3}"
