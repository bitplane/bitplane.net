Can we use deep fakes as a compression algorithm for video conference calls?

Assumptions
-----------

1. We can use facial extraction during a call to extract a user's own facial features in realtime, and send the facial model over the network to contacts.
2. We can then use facial and pose recognition to extract the position of facial features in realtime.
3. We can mask out the face region, transfer the video without the face.
4. The pose data plus the stream without a face will be smaller than the complete video stream.
5. We can compare what the person at the other end will see, with the real video, and if the differences are too much, just switch back to the full stream.


update
------

nvidia did this - so I guess it worked after all? :D
