#!/usr/bin/ruby
i = 1
j = 2
sum = 0
while j < 4000000
	if j % 2 == 0
		sum = sum + j
	end
	k = i
	i = j
	j = i + k
end
puts sum