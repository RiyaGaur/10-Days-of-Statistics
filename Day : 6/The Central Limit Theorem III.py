samples = float(input())
mean = float(input())
sd = float(input())
interval = float(input())
a = float (input())

sd_sample = sd / (samples**0.5)
print(round(mean - sd_sample*a,2))
print(round(mean + sd_sample*a,2))
