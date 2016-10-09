import static org.junit.Assert.*;
import org.junit.Test;


/**
 * Created by marshall on 7/10/16.
 */
public class isThisATriangle {
        public boolean isTriangle(int a, int b, int c) {
            if (a + b > c) {
                return true;
            } else {
                return false;
            }
        }
    }

    public class TriangleTesterTest {
        @Test
        public void publicTests() {
            assertEquals(isTriangle(1,2,2), true);
            assertEquals(isTriangle(7,2,2), false);
        }
    }
}



