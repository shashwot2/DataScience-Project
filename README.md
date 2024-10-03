# Python Google API Documentation
It's a juts basic script to run the python code which gets the data from the Google API 

## Installation
1. Install dependencies
2. Register for Google API in Google console 
3. Make an .env with the variable GOOGLE_BOOKS_API_KEY
2. run `python main.py` 



# Google Books API Data Documentation
## Overview

This document provides an overview and explanation of the dataset schema for Google Books API. The dataset provides metadata for books retrieved from the Google Books API, including information like title, author, publication details, and availability. Below is an explanation of each key present in the sample JSON object.
## JSON Schema Breakdown
### Root Object

The JSON data is an object that contains multiple properties about the book. Each property is described below:

    kind: Indicates the type of resource, here "books#volume" which represents a book volume.
    id: A unique identifier for the volume ("t16puAAACAAJ" in the sample).
    etag: A version identifier that changes whenever the volume is updated.
    selfLink: A URL to access the volume information through Google Books API.

### volumeInfo Object

This object contains core information about the book, such as:

    title: The title of the book.
        Example: "The Science Fiction Universe-- and Beyond"
    subtitle: A subtitle providing additional context for the title.
        Example: "Syfy Channel Book of Sci-fi"
    authors: A list of author names for the book.
        Example: ["Michael Mallory"]
    publisher: The name of the publisher.
        Example: "Universe Publishing(NY)"
    publishedDate: Year of publication.
        Example: "2012"
    description: A brief overview of the book's content.
    industryIdentifiers: A list of industry-standard identifiers such as ISBN.
        Types include:
            ISBN_10: 10-digit ISBN number.
            ISBN_13: 13-digit ISBN number.
    readingModes: Information on the reading format:
        text: Whether text view is available (true/false).
        image: Whether an image view is available (true/false).
    pageCount: The number of pages in the book. Here, it's 0 which may indicate missing data.
    printType: The type of content, typically "BOOK".
    categories: A list of book categories or genres.
        Example: ["Science fiction films"]
    maturityRating: Indicates content rating such as "NOT_MATURE".
    allowAnonLogging: Whether anonymous users can log view activity.
    contentVersion: Version of the content ("preview-1.0.0").
    panelizationSummary: Information about panelization in e-books:
        containsEpubBubbles: Presence of epub bubbles.
        containsImageBubbles: Presence of image bubbles.
    imageLinks: URLs for book cover images.
        smallThumbnail and thumbnail: Links to different sizes of the book cover.
    language: Language code for the book, such as "en" for English.
    previewLink: A link to preview the book on Google Books.
    infoLink: A link to more information about the book.
    canonicalVolumeLink: The canonical link to the book.

### saleInfo Object

This object provides details about the sale status of the book:

    country: Country code where the sale information applies, such as "US".
    saleability: Whether the book is available for sale, "NOT_FOR_SALE" here.
    isEbook: Boolean indicating if the book is available as an ebook.

### accessInfo Object

This object contains information regarding access to the book's content:

    country: Country where access is allowed ("US").
    viewability: The extent of the book that can be viewed, such as "NO_PAGES".
    embeddable: Whether the book can be embedded elsewhere.
    publicDomain: Whether the book is in the public domain.
    textToSpeechPermission: Whether text-to-speech is allowed.
    epub and pdf: Availability of the book in these formats.
        isAvailable: Whether the format is available.
    webReaderLink: Link to read the book in the Google Play web reader.
    accessViewStatus: The status of access ("NONE").
    quoteSharingAllowed: Whether quotes from the book can be shared.

### searchInfo Object

This object contains additional search-related information:

    textSnippet: A snippet of text from the book, helpful for previews or search indexing.