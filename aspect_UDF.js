// This is a file that describes a PostgreSQL user defined function, UDF, checking whether two astonomical bodies are within
// x degrees of one another on the eliptic from a terrestrial perspective.  This file is uploaded and working on an AWS RDS
// PostgreSQL instance.  It was originally written in python and was converted to javascript as the AWS RDS services does
// not support python for UDFs.  I know nothing of javascript so it was an exercise in methodicl conversion.

Create language plv8;

DROP FUNCTION check_for_aspect(displacement integer, orb integer, body1_position float, body2_position float);
CREATE OR REPLACE FUNCTION check_for_aspect(displacement integer, orb integer, body1_position float, body2_position float)
RETURNS boolean AS $$
    function adjust_360(degree) {
        if (degree >= 360) {
            var adjusted_degree = degree - 360;
        } else if (degree < 0) {
            var adjusted_degree = degree + 360;
        } else {
            var adjusted_degree = degree;
        }
        return adjusted_degree;
    }

    function any(iterable) {
        for (var index = 0; index < iterable.length; ++index) {
            if (iterable[index]) return true;
        }
        return false;
    }

    var result = [];
    var aspect_points = [];
    
    if ((displacement == 0) || (displacement == 180)) {
        var x = (body1_position + displacement);
        var adjust_x = adjust_360(x);
        aspect_points.push(adjust_x);
    } else {
        var y = (body1_position - displacement);
        var adjust_y = adjust_360(y);
        aspect_points.push(adjust_y);
        var z = (body1_position + displacement);
        var adjust_z = adjust_360(z);
        aspect_points.push(adjust_z);
    }

    for (var index = 0; index < aspect_points.length; index++) {
        if (aspect_points[index] < orb) {
            aspect_points[index] += 360;
        }
        if (body2_position < orb) {
            body2_position += 360;
        }
        var w = aspect_points[index] - orb
        var lower_bound = adjust_360(w);
        var upper_bound = aspect_points[index] + orb ;

        if ((lower_bound <= body2_position) && (body2_position < upper_bound)) {
            result.push(true);
        } else {
            result.push(false);
        }
    }
    return any(result);
$$
LANGUAGE plv8;
