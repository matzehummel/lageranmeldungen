// constants.js
export const currentYear = 2025;
export const minBirthday = new Date("2011-01-01");  // Minimum birthday date, should not be older than 14 years
export const maxBirthday = new Date("2016-08-01");  // Maximum birthday date, should not be younger than 9 years

export const minYear = minBirthday.getFullYear();
export const maxYear = maxBirthday.getFullYear();