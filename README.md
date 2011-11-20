# DUE ON NOVEMBER 30TH

*Authors:* John Moeller, Amirali Abdullah, Alex Clemmer

# TODO List
* (Week of November 14) 
  <2011-11-14 Mon>-<2011-11-21 Mon>

1. Find/generate new data set:
   * High dimensional
     - [John] Note that this shouldn't be *too* high dimensional; I have a gut feeling that we'll be exponential in $d$
   * Random??
     + Dirichlet would be a good choice
     + vector of independent Gammas (which is essentially unnormalized Dirichlet)
   * [Amir] Find dataset where heuristic is awful.

2. ~~Decide IO format for dataset~~
   * ~~Permutable~~
     - [John] ~~What does this mean? Lists of things are permutable.~~
   * ~~Should be easy to process~~
   * ~~Data points should be in TSV or CSV (Tab- or Comma-Separated Values)~~
   * ~~One point per line~~

3. ~~Decide trivial heuristic, code it up this week~~
   * ~~(*e.g.*, start with a point, extend it)~~
     - [John] ~~Guess who forgot to do this?~~

4. [John] Code up non-streaming case.

5. Find out how to use the package
   * [Alex] Given a ball a right-ball in a convex measure, *e.g.*, { x | D(x, c) \le r }, determine how to feed this to the package.