Intro
=====

Subjective star-based or numerical rating systems suffer from psychological
biases, based around saving space for better things, or not wanting to be too
harsh with your ratings.

 * On IMDB, users tend to save a rating of ten to mean their favourite films,
   and a seven to mean worth watching. This leaves most films that are worth
   watching score a 7, 8 or 9, with the ordering in these groups coming
   entirely from aggregate scores.
 * You don't want to give the customer support agent less than five stars,
   because it'll affect their stats.
 * If you buy a product on Amazon and aren't unhappy with it, then it gets
   four or five stars. It might as well have been a thumbs up/down.

You can fix this somewhat by adding more numbers to the range, e.g. making it
a percentage, but then you need a strict set of scoring rules to evaluate
against or--unless you've got superhuman memory or can tweak existing scores--
the ordering becomes internally inconsistent as more similar items are scored.

__I don't have any evidence to back up these claims, so maybe gathering that
would be a good idea.__

But anyway, rather than directly collect numerical ratings, we could save the
order of pairs of things based on some subjective measure, then combine
linked and overlapping pairs to give rank order. For example:

 * Richard Pyror is funnier than Gene Wilder
 * Metal is more fun than Jazz
 * The Evil Dead is scarier than Drag Me To Hell
 * My microwave is easier to use than my TV


Combining lists
---------------

The component data of a list breaks down into a bunch of facts in the form:

"`subject` thinks that `object1` has more `measure` than `object2`"

The client side can ensure that each `subject`'s list for each `measure` is
internally complete (each item is linked to another) and consistent (there's
no contradictions), the real problem is how to merge these lists into a larger
one.


