const spyPlaces = require("../src/spyPlaces");

it("should be replaced with a descriptive message", () => {
  expect(spyPlaces()).toEqual("something");
});
