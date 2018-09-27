// This sript is a user defined function, UDF, that is uploaded into an AWS RDS PostgreSQL instance.  The script is
// called via a SQL ORDER BY HAVERSINE() command.  It computes the haversine distance between two point lat/lon degree
// coordinates stored in the database.  The script was originally written in python.  AWS does not support python for UDFs
// for the RDS service so I had to convert python to javascript.  I know nothing of or about javascript so it was an
// acrobatic exercise of sorts logically and incrementally working through the conversion process.

Create language plv8;

CREATE OR REPLACE FUNCTION haversine(lat1 float, lon1 float, lat2 float, lon2 float)
RETURNS float AS $$
    var r = 6371; //earth's radius in km
    function convert_to_radians(degree) {
        var radians = degree * Math.PI / 180.0;
        return radians;
    }
    
    var rlat1 = convert_to_radians(lat1);
    var rlon1 = convert_to_radians(lon1);
    var rlat2 = convert_to_radians(lat2);
    var rlon2 = convert_to_radians(lon2);

    var h = 2 * r * Math.asin(Math.sqrt(Math.pow(Math.sin((rlat2 - rlat1)/2), 2) + (Math.cos(rlat1) * Math.cos(rlat2) * Math.pow(Math.sin((rlon2 - rlon1)/2), 2))));
    return h;
$$
LANGUAGE plv8;
