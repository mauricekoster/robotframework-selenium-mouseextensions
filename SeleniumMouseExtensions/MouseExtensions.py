from SeleniumLibrary.base import LibraryComponent, keyword
from selenium.webdriver.common.action_chains import ActionChains


class SeleniumMouseExtensions(LibraryComponent):
    def __init__(self, ctx):
        LibraryComponent.__init__(self, ctx)

    @keyword
    def mouse_down_with_offset(self, locator, xoffset, yoffset):
        """Simulates pressing the left mouse button on the element ``locator`` with the specified offset.
        See the `Locating elements` section for details about the locator
        syntax.

        Offsets are relative to the top-left corner of the element.
        Args:
        locator: The WebElement to move to.
        xoffset: X offset to move to.
        yoffset: Y offset to move to.

        The element is pressed without releasing the mouse button.
        See also the more specific keywords `Mouse Down On Image` and
        `Mouse Down On Link`.
        """
        self.info("Simulating Mouse Down on element '%s' with offset (%s, %s)." % (locator, xoffset, yoffset))
        element = self.find_element(locator)
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(element, int(xoffset), int(yoffset))
        action.click_and_hold().perform()

    @keyword
    def mouse_move_to_element_with_offset(self, locator, xoffset, yoffset):
        """Simulates moving the mouse cursor to the element ``locator`` with the specified offset.
        See the `Locating elements` section for details about the locator
        syntax.

        Move the mouse by an offset of the specified element.
        Offsets are relative to the top-left corner of the element.
        Args:
        locator: The WebElement to move to.
        xoffset: X offset to move to.
        yoffset: Y offset to move to.

        """
        self.info("Simulating Mouse Move to element '%s' with offset (%s, %s)." % (locator, xoffset, yoffset))
        element = self.find_element(locator)
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(element, xoffset, yoffset).perform()

    @keyword
    def mouse_move_by_offset(self, xoffset, yoffset):
        """Moving the mouse to an offset from current mouse position.

        Args:
        xoffset: X offset to move to, as a positive or negative integer.
        yoffset: Y offset to move to, as a positive or negative integer.

        """
        self.info("Simulating Mouse Move By Offset ({0}, {1})".format(xoffset, yoffset))
        action = ActionChains(self.driver)
        action.move_by_offset(int(xoffset), int(yoffset)).perform()

    @keyword
    def mouse_up(self, locator=None):
        """Simulates releasing the left mouse button on the element ``locator``.
        See the `Locating elements` section for details about the locator
        syntax.

        If locator is not given the mouse is released on current position.
        """
        if locator:
            self.info("Simulating Mouse Up on element '%s'." % locator)
            element = self.find_element(locator)
            ActionChains(self.driver).release(element).perform()
        else:
            self.info("Simulating Mouse Up.")
            ActionChains(self.driver).release().perform()
