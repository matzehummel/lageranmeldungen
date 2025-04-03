// constants.js
export const currentYear = 2025;
export const maxBirthday = new Date("2012-01-01");  // Maximum birthday date, should not be younger than 13 years
export const minBirthday = new Date("2008-01-01");  // Minimum birthday date, should not be older than 17 years

export const minYear = minBirthday.getFullYear();
export const maxYear = maxBirthday.getFullYear();