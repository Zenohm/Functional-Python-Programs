import os
import sys


def time_convert(time_in_seconds):
    if not time_in_seconds:
        return 0
    elif not time_in_seconds // 1:
        # Subsecond conversions first
        time_in_seconds *= .1
        table_of_conversions = [('yoctoseconds', 0.000000000000000000000001), ('zeptoseconds', 0.000000000000000000001),
                                ('attoseconds', 0.000000000000000001), ('femtoseconds', 0.000000000000001),
                                ('picoseconds', 0.000000000001), ('nanoseconds', 0.000000001),
                                ('microseconds', 0.000001), ('milliseconds', 0.001), ('centiseconds', 0.01),
                                ('deciseconds', 0.1), ('seconds', 1)]
        for converter_unit in range(len(table_of_conversions)):
            if time_in_seconds - table_of_conversions[converter_unit][1] <= 0:
                return '{0} {1}'.format(10 * time_in_seconds / table_of_conversions[converter_unit][1],
                                        table_of_conversions[converter_unit][0])
    else:
        # Supersecond conversions last
        table_of_conversions = [('ages-of-the-universe', 440294400000000000), ('millennia', 31449600000),
                                ('centuries', 3144960000), ('years', 31449600), ('weeks', 604800), ('days', 86400),
                                ('hours', 3600), ('minutes', 60), ('seconds', 1)]
        for converter_unit in range(len(table_of_conversions)):
            if time_in_seconds - table_of_conversions[converter_unit][1] > 0:
                return '{0} {1}'.format(time_in_seconds / table_of_conversions[converter_unit][1],
                                        table_of_conversions[converter_unit][0])
            elif converter_unit == len(table_of_conversions) - 1:
                return str(time_in_seconds) + ' seconds'


def passwordpower(password, mode=1):
    if password == '' or password == ' ':
        return 0
    import math

    passwordscore, characters, response = 0, list(password), False
    entropypool = 0
    results = {'uppercase': 0, 'lowercase': 0, 'numbers': 0, 'special': 0}
    powercheck = {'uppercase': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'lowercase': 'abcdefghijklmnopqrstuvwxyz',
                  'numbers': '1234567890', 'special': """ `~!@#$%^&*()_-+={[]}|\:;"'<,>.?/*"""}
    for currentcharacter in characters:
        for currentcheck in powercheck:
            if currentcharacter in powercheck[currentcheck]:
                results['{}'.format(currentcheck)] += 1
    # Puts the contents of the '10k most commonly used passwords' file, from the current operating directory, into a list
    commonpasswordslist = ''.join([p.replace('\n', ' ') for p in
                                   open(os.path.join(os.path.split(sys.argv[0])[0], '10k most common.txt'),
                                        'r')]).split()
    length, entropypool = 1, 1
    if password in commonpasswordslist:
        response = True
        for currentscore in results:
            if results[currentscore]:
                passwordscore += 1
        entropypool, length = 10000, 1
    else:
        for currentscore in results:
            if results[currentscore]:
                passwordscore += 1
                entropypool += len(powercheck['{}'.format(currentscore)])
        length = len(password)
    if not passwordscore:
        passwordscore += 1
    approximate_max_time_to_compute = time_convert((2 ** (length * math.log(entropypool))) / 350000000000)
    bitentropy = length * math.log(entropypool, 2)
    PowerAcclimationRatio = 1000 * float(approximate_max_time_to_compute.split()[0]) / (
        passwordscore * length * math.log(entropypool, 2))
    rankings = {'ages-of-the-universe': "Crackers' Bane", 'millennia': 'Extremely Secure', 'centuries': 'Very Secure',
                'years': 'Secure', 'weeks': 'Mediocre Security', 'days': 'Insecure', 'hours': 'Very Insecure',
                'minutes': 'Extremely Insecure', 'seconds': 'Dangerously Insecure'}
    try:
        safetysticker = rankings['{}'.format(approximate_max_time_to_compute.split()[1])]
    except:
        safetysticker = "Instantaneous Cracking"
    if response == True:
        safetysticker = 'This is one of the 10,000 most used passwords, it would be cracked almost instantaneously.'
    statistics = {'score': passwordscore, 'length': len(password), 'common': response, 'bitentropy': bitentropy,
                  'maxtime': approximate_max_time_to_compute, 'PowerAcclimationRatio': PowerAcclimationRatio,
                  'Safety': safetysticker}
    if mode:
        print(
            "\n--Scores--\n\nPower-Acclimation Ratio: {0}\nPassword Variety Score (Out of 4): {1}\n\n--Password Information--\n\nBit Entropy: {2}\nPassword Length: {3}\nCommon: {4}\nMaximum Time Required to Break Password: {5}\nPassword Safety: {6}\n".format(
                PowerAcclimationRatio, passwordscore, bitentropy, len(password), response,
                approximate_max_time_to_compute,
                safetysticker))
    else:
        return statistics


passwordpower(input("Enter Password:"))
input("\nOperations Complete. Press Enter to Exit...")