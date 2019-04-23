# Weekly report 6

## To do
-[ ] Find a way to resample the data into binary fashion. For example, for classes a,b,c,d, I want class a and class not
a(including b,c,d, but the sum should be only at the same amount of a) Example, we have 100 images for each class a,b,c,d
the combined class not-a class should have 33 from each b,c, and d with random selection.  

-[ ] Using for loop to count how many data points in each class is slow. Need to speed that up next week

-[ ] The make_balanced_dataloader might have some issue with the last image for each class, need to test that next week

-[ ] So now, there are two ways of doing this:
    -[ ] First, I created a balanced training dataset, small training expense with lower untarget accuracy 
    -[ ] Second, I train the network without the balance. It should get better performance overall.
    -[ ] Then I realized the unbalanced data may not work, especially when I have multiple class. The reason is the model 
    will just predict it's not the value we want. This no-brainer can easily leads to over 83% accuracy in a 6 classes 
    situation.
## Finished

-[x] About the attributes problem, it turned out that the torchvision package was not up-to-dated. Both Conda and Pip only had 0.2.1 version. The latest 
is 0.2.3. I installed from source and it's working now.

-[x] I found a useful function in the pytorch forum. [Link](https://discuss.pytorch.org/t/balanced-sampling-between-classes-with-torchvision-dataloader/2703/3)

-[x] I was having a bug of out bound of dimenson. It's because the last batch size is not the multiple of the batch
size. Use len(labels) resolve the problem.