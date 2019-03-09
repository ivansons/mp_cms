/**
 * Copyright (c) 2003-2015, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.md or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
  // Define changes to default configuration here. For example:
  // config.language = 'fr';
  // config.uiColor = '#AADC6E';

  // Prevent Lorem Ipsum default text from showing when an image is selected
  // for a post.  Note that empty string will not work as the OR logic in the
  // /ckeditor/ckeditor/plugins/image/dialogs/image.js will select the Lorem
  // Ipsum text when ORed with empty string
  config.image_previewText = " ";
};
