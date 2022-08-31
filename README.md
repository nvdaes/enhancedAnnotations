# Enhanced Annotations #

*	Authors: George Kerscher, Noelia Ruiz Martínez
* [download stable version][1] (compatible with NVDA 2022.1 and beyond)

In the DAISY Consortium, best practices are developed for publishers and authors for providing extended (long) descriptions.

The best practices use the HTML details element that follows the image, or a link to another file that contains the extended description.

In both options, the user would need to move to the details or the link and activate it.

Having a keystroke to put focus on the details or the link is ideal. 

Our best practices recommend that the details or the link immediately follows the image, and if the link is followed, a back link to the exact location must be provided. This makes it certain that the user will not get lost.

However it is probable that authors in the wild will place the extended (long) description almost anywhere. In these cases, the user would want to return to the image and hence the need for a way to return to the original image.

This add-on provides both features, in support of this [issue opened in NVDA's repository][2].

## Commands ##

* NVDA+alt+d: moves the cursor to the element identified with aria-details.
* NVDA+alt+shift+d: moves the cursor to the original element, for example, an image with furter details like a long description.

The above commands can be modified from NVDA's menu, Preferences submenu, Input gestures dialog, Browse mode category.

[1]: https://addons.nvda-project.org/files/get.php?file=enhancedannotations

[2]: https://github.com/nvaccess/nvda/issues/13940
