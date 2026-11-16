"""Unit AS5: Sampling methods (OCR MEI Sx1–Sx3, IAL S3 2.1–2.2; S2 4.1 terms)."""

RANDOM_ROWS = [
    "31948 26373 11482 22114 31714 29848 79198 40037",
    "52014 84948 36865 86247 40920 47801 20436 50716",
    "79193 01661 89771 32120 29956 04179 70295 01983",
    "25340 35861 03235 87580 58084 14302 56311 66282",
]

UNIT = {
    "number": "AS5",
    "title": "Sampling methods",
    "tag": "AS · OCR MEI Sx1–Sx3, IAL S3 2.1–2.2 (with the S2 4.1 vocabulary) · prior knowledge for CAIE 9231 "
           "and useful background for every board's hypothesis tests",
    "notes": [
        ("p", "Almost every result in statistics starts with a sample. A test or a confidence interval is only as good as the "
              "data behind it, so you need to know how samples are chosen, what can go wrong, and why random sampling "
              "matters. This unit is mostly about ideas and vocabulary, but stratified allocation, systematic intervals and "
              "random-number selection are routine calculations that examiners set every year."),

        ("h2", "5.1 Populations, samples and censuses"),
        ("bullets", [
            "<b>Population</b>: the whole set of items (people, objects, events) you want to know about. A population can be "
            "finite (the 1200 pupils in a school) or effectively infinite (all the bolts a machine will ever make).",
            "<b>Census</b>: data collected from every member of the population.",
            "<b>Sample</b>: a subset of the population, used to learn about the whole population.",
            "<b>Sampling unit</b>: one individual member that can be sampled (one pupil, one bolt, one household).",
            "<b>Sampling frame</b>: a list (or map, or numbering) of all the sampling units, from which the sample is drawn. "
            "An electoral register, a school roll and a numbered list of invoices are sampling frames.",
            "<b>Parameter</b>: a numerical property of the population, such as the population mean μ or proportion p. "
            "It is usually unknown.",
            "<b>Statistic</b>: a quantity calculated from the sample only, such as the sample mean x̄. A statistic varies "
            "from sample to sample; its probability distribution is its <b>sampling distribution</b>.",
        ]),
        ("table", ["", "Census", "Sample"], [
            ["Accuracy", "Exact answer for the population (apart from recording errors)", "Estimate only; subject to sampling variation and possible bias"],
            ["Cost and time", "Expensive and slow for a large population", "Cheaper and quicker; data can be checked more carefully"],
            ["Destructive testing", "Impossible: testing everything destroys the population", "The only option (e.g. lifetime of light bulbs, crash tests)"],
            ["Best used when", "The population is small, or every member matters (e.g. a register of patients)", "The population is large, testing is destructive, or results are needed quickly"],
        ]),
        ("p", "A sampling frame should match the population. If it leaves out part of the population (for example a "
              "telephone directory leaves out people with no landline), even a perfectly random selection from the frame is biased."),

        ("h2", "5.2 Good samples, bias and why randomness matters (OCR MEI Sx2, Sx3)"),
        ("p", "A good sample is <b>representative</b>: it looks like the population in the ways that matter for the "
              "question. A sampling method is <b>biased</b> if it tends to give samples that systematically over- or "
              "under-represent part of the population, so that estimates are consistently too high or too low. Bias does "
              "not go away when the sample gets bigger; a large biased sample just gives a precise wrong answer."),
        ("bullets", [
            "<b>Selection bias</b>: the method favours some units, e.g. surveying shoppers at 11 am on a weekday misses most full-time workers.",
            "<b>Frame bias</b>: the sampling frame is incomplete or out of date.",
            "<b>Non-response bias</b>: people who do not reply may differ from those who do (busy people return fewer questionnaires).",
            "<b>Response bias</b>: answers are inaccurate, e.g. a leading question, or people giving the answer they think is wanted.",
            "<b>Self-selection</b>: volunteers (phone-in polls, online ratings) tend to have strong opinions.",
        ]),
        ("box", "Why a random sample is needed for inference", [
            "In a <b>random</b> sample, chance alone decides which units are chosen, so no part of the population is favoured "
            "and the method is free from selection bias.",
            "Because the selection is governed by probability, the sampling distribution of a statistic can be worked out. "
            "This is what lets you calculate p-values, critical regions and confidence intervals.",
            "With a non-random sample (quota, opportunity, self-selected) there is no probability model for the selection, "
            "so the results of a hypothesis test or a confidence interval cannot be relied on.",
        ]),

        ("h2", "5.3 Simple random sampling and random numbers (IAL S3 2.1)"),
        ("p", "A <b>simple random sample</b> of size n is one chosen so that <b>every possible sample of size n is equally "
              "likely</b> to be selected. In particular, every unit has the same chance n/N of being chosen. It needs a "
              "sampling frame. Sampling is normally <b>without replacement</b>: a unit chosen twice is used only once."),
        ("bullets", [
            "<b>Lottery method</b>: write each unit's name or number on a ticket, mix them thoroughly and draw n tickets. "
            "Practical only for small populations.",
            "<b>Random number method</b>: number the frame using the same number of digits for every unit (01 to 80, or "
            "001 to 450). Read digits from a random number table (or a calculator's Ran# function) in groups of that "
            "length. Ignore groups outside the range and ignore repeats. Continue until n units are chosen.",
        ]),
        ("p", "The digits below are a section of a random number table, used in the examples and practice in this unit. "
              "Read along each row from left to right; the spaces are only to make the digits easier to read."),
        ("table", ["Row", "Random digits"], [[str(i + 1), r] for i, r in enumerate(RANDOM_ROWS)]),
        ("table", ["Simple random sampling", ""], [
            ["Advantages", "Free of selection bias; easy to understand; the standard probability results apply directly."],
            ["Disadvantages", "Needs a full sampling frame; impractical for large or spread-out populations; by chance the sample "
                              "may not be representative of important groups (e.g. no Year 13 pupils at all)."],
        ]),

        ("h2", "5.4 Systematic sampling (IAL S3 2.2)"),
        ("p", "To choose n items from an ordered list of N: find the interval k = N/n (round down if it is not a whole "
              "number). Choose a random starting point among the first k items, then take every kth item after it."),
        ("bullets", [
            "Advantages: simple and quick, especially when items are produced or listed in order (a production line, invoices "
            "in a file); spreads the sample evenly across the list.",
            "Disadvantages: needs an ordered frame; it is not a simple random sample, because most samples of size n cannot occur; "
            "it is biased if the list has a pattern with period related to k (for example every 10th flat on a list being a "
            "corner flat).",
        ]),

        ("h2", "5.5 Stratified sampling (IAL S3 2.2)"),
        ("p", "When the population divides into distinct groups (<b>strata</b>, singular stratum) that differ in ways that "
              "matter, take a separate simple random sample from each stratum. With <b>proportional allocation</b> each "
              "stratum contributes in proportion to its size."),
        ("box", "Proportional allocation", [
            "Number sampled from stratum i = (size of stratum i ÷ population size) × total sample size, i.e. nᵢ = n × Nᵢ / N.",
            "Round to whole numbers and check that the numbers add up to n. If rounding to the nearest whole number gives a "
            "total of n + 1 or n − 1, adjust the stratum whose value was closest to the half-way point, and say so.",
            "Within each stratum, select the units by simple random sampling (or another random method).",
        ]),
        ("bullets", [
            "Advantages: guarantees every stratum is represented in the right proportion; usually gives more precise estimates "
            "than a simple random sample of the same size; also gives estimates for each stratum separately.",
            "Disadvantages: needs a sampling frame for every stratum and knowledge of stratum sizes; strata must be clearly "
            "defined and must not overlap; more complex to organise.",
        ]),

        ("h2", "5.6 Quota, cluster and opportunity sampling"),
        ("p", "<b>Quota sampling</b> (IAL S3 2.2) is the non-random version of stratified sampling. The interviewer is told "
              "how many people to interview from each group (for example 21 full-time men, 18 full-time women, …) and fills "
              "each quota with whoever they meet, until it is full."),
        ("bullets", [
            "Quota advantages: no sampling frame needed; quick and cheap; the sample matches the population in the chosen "
            "characteristics; non-response is not a problem (the interviewer simply asks someone else).",
            "Quota disadvantages: not random, so it can be biased (the interviewer chooses who to approach and where to "
            "stand); people who refuse are replaced, which hides non-response bias; probability results cannot strictly be applied.",
            "<b>Cluster sampling</b>: the population is naturally in groups (<b>clusters</b>) such as schools, streets or "
            "boxes. Choose some clusters at random and sample every unit in them (or a random sample within them). It is "
            "cheap when the population is spread over a wide area, but units in a cluster are often alike, so it is less "
            "precise than a simple random sample of the same size. Clusters should each be like a miniature population; "
            "strata, by contrast, should each be as alike inside as possible.",
            "<b>Opportunity (convenience) sampling</b>: use the units that happen to be available, e.g. the first 30 people "
            "to walk past. Very easy and cheap, but very likely to be unrepresentative and biased.",
            "<b>Self-selected (volunteer) sampling</b>: people choose to take part. Easy, but respondents tend to have strong views.",
        ]),

        ("h2", "5.7 Sample size and effect size (OCR MEI Sx1)"),
        ("p", "Bigger random samples give more precise estimates. If the population standard deviation is σ, the sample mean "
              "of a random sample of size n has standard deviation σ/√n, called its <b>standard error</b>. Because of the "
              "square root, halving the standard error needs four times the sample size."),
        ("p", "In an experiment the <b>effect size</b> is the size of the difference you are trying to detect (for example "
              "a new fertiliser increasing mean yield by 2 kg per plant). A small effect is easily hidden by random "
              "variation, so it needs a large sample to show up as significant; a large effect can be detected with a small "
              "sample. Choosing the sample size is therefore part of designing the experiment, not an afterthought. "
              "Remember that size cannot cure bias: a larger sample reduces random error, not systematic error."),

        ("h2", "5.8 Choosing a method"),
        ("table", ["Method", "Random?", "Frame needed?", "Typical use"], [
            ["Simple random", "Yes", "Yes, of whole population", "Small or moderate populations with a complete list"],
            ["Systematic", "Partly (random start)", "Yes, ordered", "Production lines, files, lists in order"],
            ["Stratified", "Yes, within strata", "Yes, for each stratum", "Population in distinct groups that differ, e.g. year groups, sites"],
            ["Cluster", "Yes, clusters chosen at random", "Only a list of clusters", "Large, spread-out populations (schools, towns)"],
            ["Quota", "No", "No", "Market research and opinion polls needing quick results"],
            ["Opportunity", "No", "No", "Pilot studies; whatever is to hand"],
        ]),
        ("p", "When asked to choose or criticise a method, link your answer to the context: name the strata or the frame, say "
              "which group would be missed or over-represented, and explain the effect on the results."),
        ("warn", "Common mistakes", [
            "Describing a simple random sample as one where \"everyone has an equal chance\". That is necessary but not "
            "sufficient (a systematic sample also gives everyone an equal chance). Say <i>every possible sample of size n is equally likely</i>.",
            "Using random numbers without first numbering the frame with equal-length labels, or forgetting to say that "
            "out-of-range numbers and repeats are ignored.",
            "In stratified sampling, forgetting to say that units are chosen <b>at random within each stratum</b>, or giving "
            "stratum sample sizes that do not add up to n.",
            "Calling quota sampling random. The interviewer picks the people, so it is not.",
            "Generic answers such as \"it is quicker\" with no reference to the context. Marks need a reason tied to the situation.",
            "Thinking a larger sample removes bias. It reduces sampling variability only.",
        ]),
    ],
    "examples": [
        {
            "title": "Census or sample, frame and units",
            "question": "A factory makes 5000 fuses a day. The quality manager wants to know the current at which the fuses fail. "
                        "(a) Explain why a census is not suitable. (b) Suggest a sampling frame and a sampling unit. "
                        "(c) Give one advantage of a sample over a census in this context, apart from your answer to (a).",
            "steps": [
                "(a) Finding the failure current destroys the fuse. A census would destroy the whole day's output, leaving nothing to sell.",
                "(b) Sampling unit: one fuse. Sampling frame: a numbered list of the 5000 fuses made that day (for example by "
                "order of production, 0001 to 5000).",
                "(c) A sample is quicker and cheaper to test, so results are available while the day's batch can still be held back if faulty.",
            ],
        },
        {
            "title": "Selecting a simple random sample with random numbers",
            "question": "A teacher wants a simple random sample of 6 pupils from a year group of 80. Describe how to use the random "
                        "number table in 5.3, starting at the beginning of row 1, and list the numbers of the pupils chosen.",
            "steps": [
                "Number the pupils 01 to 80 (each label has two digits) using the class lists as the sampling frame.",
                "Read row 1 in pairs: 31 94 82 63 73 11 48 22 …",
                "31 is chosen. 94 and 82 are out of range (greater than 80), so ignore them. Then 63, 73, 11, 48 and 22 are chosen.",
                "The sample is pupils 31, 63, 73, 11, 48 and 22. Any repeated number would also be ignored, so that the sample is "
                "chosen without replacement.",
            ],
        },
        {
            "title": "A systematic sample and its weakness",
            "question": "An auditor wants a sample of 30 from 600 invoices filed in date order. (a) Describe how to take a "
                        "systematic sample. (b) List the first three and the last invoice chosen if the random start is invoice 7. "
                        "(c) Give one reason why the sample might be biased.",
            "steps": [
                "(a) The interval is k = 600 ÷ 30 = 20. Number the invoices 1 to 600 in date order. Choose a random number from 1 "
                "to 20 for the start, then take every 20th invoice after it.",
                "(b) Start 7 gives 7, 27, 47, … The last is 7 + 29 × 20 = 587.",
                "(c) If the invoices have a pattern that repeats every 20 (for example if 20 invoices are filed each week, so the "
                "7th each week is always the same supplier's), the sample would contain only that type and be unrepresentative.",
            ],
        },
        {
            "title": "Stratified sample with proportional allocation",
            "question": "A school has 240 pupils in Year 7, 220 in Year 8, 210 in Year 9, 180 in Year 10 and 150 in Year 11. A "
                        "stratified sample of 60 pupils is to be taken using the year groups as strata. (a) Find how many pupils "
                        "should be sampled from each year. (b) Explain how the pupils in Year 7 would then be chosen.",
            "steps": [
                "(a) N = 240 + 220 + 210 + 180 + 150 = 1000, so each year gives (stratum size ÷ 1000) × 60.",
                "Year 7: 240 × 60/1000 = 14.4 → 14. Year 8: 13.2 → 13. Year 9: 12.6 → 13. Year 10: 10.8 → 11. Year 11: 9.0 → 9.",
                "Check: 14 + 13 + 13 + 11 + 9 = 60, as required.",
                "(b) Number the 240 Year 7 pupils 001 to 240 and use random numbers (ignoring out-of-range values and repeats) to "
                "choose 14 of them, i.e. a simple random sample within the stratum.",
            ],
        },
        {
            "title": "Quota sample versus stratified sample",
            "question": "A company has 400 employees: 168 full-time men, 144 full-time women, 32 part-time men and 56 part-time women. "
                        "A manager wants the views of 50 employees on a new canteen. (a) Find the quotas for a quota sample "
                        "of 50 that matches the workforce. (b) Explain how a stratified sample would differ, and give one "
                        "advantage of each method here.",
            "steps": [
                "(a) Each group gives (group size ÷ 400) × 50, i.e. ÷ 8: 168/8 = 21, 144/8 = 18, 32/8 = 4, 56/8 = 7. Check 21 + 18 + 4 + 7 = 50.",
                "(b) In the quota sample the manager would ask whoever is available in the canteen until each quota is full. In "
                "a stratified sample the same numbers would be chosen <b>at random</b> from a staff list for each group.",
                "Stratified: random selection avoids the manager choosing friendly or nearby staff, so it is less likely to be biased. "
                "Quota: no staff list is needed and it is quick; if someone refuses, another employee from the same group is asked.",
            ],
        },
        {
            "title": "Sample size and standard error",
            "question": "The masses of a certain apple have standard deviation 12 g. (a) Find the standard error of the mean mass "
                        "of a random sample of 36 apples. (b) How large a sample is needed for the standard error to be 1 g? "
                        "(c) A farmer wants to show that a new feed increases mean mass by about 1 g. Explain why a sample of 36 "
                        "is unlikely to be enough.",
            "steps": [
                "(a) Standard error = σ/√n = 12/√36 = 12/6 = 2 g.",
                "(b) 12/√n = 1 gives √n = 12, so n = 144. Halving the standard error needed four times the sample size.",
                "(c) With n = 36 random variation in the sample mean is about 2 g, twice the effect being looked for, so a real "
                "1 g increase would usually not be significant. A small effect size needs a large sample.",
            ],
        },
    ],
    "practice": [
        "Define each term and give an example of it for a survey of the views of members of a gym: (a) population, (b) sampling unit, (c) sampling frame.",
        "Give two reasons why a sample might be used rather than a census, and one situation in which a census is the better choice.",
        "Explain the difference between a parameter and a statistic, using the mean height of 17-year-olds in the UK as the example.",
        "A simple random sample of 5 is to be taken from 60 members of a club numbered 01 to 60. Use row 2 of the random number table in 5.3, reading pairs from the start of the row, to choose the sample.",
        "A simple random sample of 5 is to be taken from 450 houses numbered 001 to 450. Use row 3 of the random number table, reading groups of three digits from the start of the row, to choose the sample.",
        "A machine fills 1200 bottles an hour. A systematic sample of 40 bottles an hour is needed. (a) Find the sampling interval. (b) If the random start is bottle 18, find the numbers of the 2nd and the 40th bottles sampled.",
        "A college has 330 students at site A, 270 at site B and 150 at site C. Find the number of students from each site in a stratified sample of 40.",
        "A firm has three departments with 35, 35 and 30 staff. A stratified sample of 10 is required. Show that rounding each value to the nearest whole number gives the wrong total, and suggest how to resolve this.",
        "Explain why quota sampling is not random, and give one advantage and one disadvantage of quota sampling compared with stratified sampling.",
        "A council wants to survey households in a large rural county. Explain why cluster sampling might be used and give one disadvantage.",
        "A radio station asks listeners to phone in to say whether they support a new bypass. 78% of callers are against it. Explain why this may not represent the views of the town.",
        "The standard deviation of the time taken to complete a puzzle is 8 minutes. (a) Find the standard error of the mean for a random sample of 16. (b) Find the sample size needed to make the standard error 0.5 minutes.",
    ],
    "answers": [
        "(a) All members of the gym. (b) One member. (c) The gym's membership list.",
        "Any two of: cheaper; quicker; less data to process so it can be checked carefully; testing may be destructive. A census is better when the population is small or every member must be included (e.g. checking every passenger's ticket on a small flight, or a register of patients).",
        "A parameter describes the population and is fixed but usually unknown, e.g. the mean height μ of all UK 17-year-olds. A statistic is calculated from a sample, e.g. the mean height x̄ of 100 randomly chosen 17-year-olds; it varies from sample to sample and is used to estimate μ.",
        "Pairs: 52 01 48 49 48 36 … Choose 52, 01, 48, 49; the second 48 is a repeat and is ignored; then 36. Sample: 52, 01, 48, 49, 36.",
        "Groups: 791 930 166 189 771 321 202 … Ignore 791, 930 and 771 (over 450). Sample: 166, 189, 321, 202 and, after ignoring 995 and 604, 179.",
        "(a) k = 1200 ÷ 40 = 30. (b) 2nd bottle: 18 + 30 = 48. 40th bottle: 18 + 39 × 30 = 1188.",
        "N = 750. A: 330 × 40/750 = 17.6 → 18. B: 14.4 → 14. C: 8.0 → 8. Check 18 + 14 + 8 = 40.",
        "N = 100, so the values are 3.5, 3.5 and 3. Rounding to the nearest gives 4 + 4 + 3 = 11, not 10. Round one of the two 3.5s down (choose which at random, or state a reason), giving 4, 3, 3.",
        "The interviewer chooses who to ask within each quota, so selection is not governed by chance. Advantage: no sampling frame needed, quick and cheap (or non-response does not reduce the sample). Disadvantage: possible interviewer bias and hidden non-response bias, so results may be unrepresentative and probability-based inference is not strictly valid.",
        "Households are spread over a large area, so choosing a few villages (clusters) at random and surveying households in them greatly reduces travel cost and time. Disadvantage: households in the same village tend to be similar, so the sample is less precise (and may be unrepresentative) compared with a simple random sample of the same size.",
        "It is a self-selected sample: only people who listen to that station and feel strongly enough to call are included. People opposed to the bypass may be more motivated to call, so the 78% is likely to be biased.",
        "(a) 8/√16 = 2 minutes. (b) 8/√n = 0.5 gives √n = 16, so n = 256.",
    ],
    "exam": [
        "A sixth form has 180 students in Year 12 and 140 in Year 13. The head wants the views of 40 students on a new timetable.\n"
        "(a) Explain why a sampling frame is needed for a simple random sample, and suggest a suitable one. [2]\n"
        "(b) Describe how a stratified sample of 40, with year groups as strata, could be selected. Include the number from each year. [4]\n"
        "(c) Give one advantage of the stratified sample over a simple random sample in this context. [1]\n"
        "(d) The head instead suggests asking the first 40 students to arrive in the common room. Name this method and explain why it may be biased. [2]",
        "A market researcher is asked to interview 200 adults in a town centre about local transport. The town's adult population is 48% male and 52% female, and 30% are aged 65 or over.\n"
        "(a) Assuming age and sex are independent in the population, find the quota for women aged 65 or over. [2]\n"
        "(b) Give two reasons why the researcher might use quota sampling rather than stratified sampling. [2]\n"
        "(c) Explain how interviewing only between 10 am and 2 pm on weekdays could bias the results, even though every quota is filled. [2]\n"
        "(d) State whether a hypothesis test based on the quota sample would be valid, giving a reason. [1]",
        "A biologist has a list of 2400 trees in a forest, numbered 0001 to 2400, and wants to estimate their mean height.\n"
        "(a) Explain why a random sample is needed if she wants to use her estimate in a confidence interval. [1]\n"
        "(b) Describe how to choose a systematic sample of 60 trees from the list, and state the probability that a particular tree is chosen. [3]\n"
        "(c) Explain why a systematic sample is not a simple random sample. [1]\n"
        "(d) The standard deviation of tree heights is believed to be 4.5 m. Find the standard error of the sample mean for a random sample of 60 trees, giving your answer to 3 significant figures. [2]\n"
        "(e) She wants the standard error to be at most 0.3 m. Find the smallest sample size needed. [2]",
        "A hospital trust has 4 hospitals with 520, 410, 300 and 270 nurses. The trust wants to survey 75 nurses about working hours.\n"
        "(a) Find the number to be sampled from each hospital using a stratified sample with proportional allocation. [3]\n"
        "(b) The trust suggests choosing one hospital at random and surveying 75 nurses there. Name this type of sampling and give one advantage and one disadvantage. [3]\n"
        "(c) Only 46 of the 75 nurses chosen for the stratified sample return the questionnaire. Explain how this might bias the results, and suggest one way of reducing the problem. [2]",
    ],
    "exam_answers": [
        "(a) A simple random sample needs every student to be numbered so that random numbers can pick them [B1]; e.g. the school's list of all 320 sixth-form students [B1].\n"
        "(b) Year 12: 180/320 × 40 = 22.5; Year 13: 140/320 × 40 = 17.5 [M1]. Rounding both up would give 41, so take 23 and 17 (or 22 and 18), stating the choice [A1]. "
        "Number each year group's list (e.g. 001–180 and 001–140) [M1] and use random numbers, ignoring repeats and out-of-range values, to choose the required number from each year [A1].\n"
        "(c) It guarantees both year groups are represented in proportion, and Year 12 and Year 13 views may differ [B1].\n"
        "(d) Opportunity (convenience) sampling [B1]. Students who arrive early or use the common room may have different timetables or views (e.g. study-period students), so they may not represent all students [B1].",
        "(a) 0.52 × 0.30 × 200 [M1] = 31.2, so 31 women aged 65+ [A1].\n"
        "(b) Any two: no sampling frame of town-centre users is available; quicker and cheaper; results are needed quickly; non-response is handled by replacing refusals [B1 B1].\n"
        "(c) People in work or education are rarely in town on weekday daytimes, so those filling the quotas are mainly retired, unemployed or part-time people [B1]; their transport use (e.g. off-peak bus travel rather than commuting) may differ, so the views are unrepresentative [B1].\n"
        "(d) Not strictly valid: the sample is not random, so the sampling distribution of the test statistic is not known [B1].",
        "(a) The theory of confidence intervals (the sampling distribution of x̄) assumes random selection; without it the sample may be biased and the stated confidence level is meaningless [B1].\n"
        "(b) k = 2400 ÷ 60 = 40 [B1]. Choose a random number from 01 to 40 as the start, then take every 40th tree on the list [M1]. P(a given tree chosen) = 1/40 = 0.025 [A1].\n"
        "(c) Only 40 different samples are possible (one for each start), so not every sample of 60 trees is equally likely; e.g. trees 0001 and 0002 can never both be chosen [B1].\n"
        "(d) SE = 4.5/√60 [M1] = 0.581 m (3 s.f.) [A1].\n"
        "(e) 4.5/√n ≤ 0.3 gives √n ≥ 15 [M1], so n ≥ 225; the smallest sample size is 225 [A1].",
        "(a) N = 1500, so multiply each by 75/1500 = 0.05 [M1]: 26, 20.5, 15, 13.5 [A1]. Rounding both halves up would give 76, so take 26, 21, 15, 13 (or 26, 20, 15, 14), stating the adjustment so the total is 75 [A1].\n"
        "(b) Cluster sampling (one cluster) [B1]. Advantage: cheaper and simpler to organise, as only one site is visited [B1]. Disadvantage: nurses at one hospital share the same management and shift patterns, so they may not represent the whole trust [B1].\n"
        "(c) Non-response bias: nurses working the longest hours may be too busy to reply (or the most dissatisfied may be keenest to reply), so the replies may not reflect all nurses [B1]. Send reminders, allow online replies, or follow up non-responders (or replace them at random from the same hospital) [B1].",
    ],
}
