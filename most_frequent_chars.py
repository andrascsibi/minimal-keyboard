#!/usr/bin/env python2.6

english = [
  ('e', 12.70),
  ('t', 9.056),
  ('a', 8.167),
  ('o', 7.507),
  ('i', 6.966),
  ('n', 6.749),
  ('s', 6.327),
  ('h', 6.094),
  ('r', 5.987),
  ('d', 4.253),
  ('l', 4.025),
  ('c', 2.782),
  ('u', 2.758),
  ('m', 2.406),
  ('w', 2.360),
  ('f', 2.228),
  ('g', 2.015),
  ('y', 1.974),
  ('p', 1.929),
  ('b', 1.492),
  ('v', 0.978),
  ('k', 0.772),
  ('j', 0.153),
  ('x', 0.150),
  ('q', 0.095),
  ('z', 0.074)
]

hungarian = [
  ('e', 12.256),
  ('a', 9.428),
  ('t', 7.380),
  ('n', 6.445),
  ('l', 6.383),
  ('s', 5.322),
  ('k', 4.522),
  ('e', 4.511),
  ('i', 4.200),
  ('m', 4.054),
  ('o', 3.867),
  ('a', 3.649),
  ('g', 2.838),
  ('r', 2.807),
  ('z', 2.734),
  ('v', 2.453),
  ('b', 2.058),
  ('d', 2.037),
  ('s', 1.809),
  ('z', 1.809),
  ('j', 1.570),
  ('h', 1.341),
  ('g', 1.185),
  ('y', 1.185),
  ('o', 0.884),
  ('o', 0.821),
  ('n', 0.790),
  ('y', 0.790),
  ('l', 0.738),
  ('y', 0.738),
  ('u', 0.655),
  ('o', 0.634),
  ('f', 0.582),
  ('p', 0.509),
  ('i', 0.499),
  ('u', 0.416),
  ('c', 0.260),
  ('s', 0.260),
  ('u', 0.125),
  ('c', 0.114),
  ('u', 0.104),
  ('z', 0.021),
  ('s', 0.021),
  ('q', 0),
  ('x', 0),
  ('w', 0)
]

def score_sorted(a):
  return sorted(a, key=lambda x: -x[1])

def char_sorted(a):
  return sorted(a, key=lambda x: x[0])

def normalize(ch_array):
  scores = {}
  for c, freq in ch_array:
    scores[c] = scores.get(c, 0) + freq
  total = sum(scores.values())
  normalized = []
  for c, freq in scores.items():
    normalized.append((c, freq / total))
  return char_sorted(normalized)

english = normalize(english)
hungarian = normalize(hungarian)

combined = []
for e, h in zip(english, hungarian):
  combined.append((e[0], e[1] + h[1]))
for c, s in score_sorted(combined):
  print "%s   (%s)" % (c, s)


